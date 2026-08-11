import api from "./api";

import { useAuthStore } from "@/store/auth.store";

import type {
  ChatRequest,
  ChatResponse,
} from "@/types/chat";


class ChatService {

  // ========================================================
  // NORMAL CHAT
  // ========================================================

  async sendMessage(
    data: ChatRequest,
  ): Promise<ChatResponse> {

    const response = await api.post(
      "/chat",
      data,
    );

    return response.data;
  }


  // ========================================================
  // STREAMING CHAT
  // ========================================================

  async streamMessage(
    data: ChatRequest,
    onToken: (token: string) => void,
  ): Promise<number> {

    const token =
      useAuthStore.getState().accessToken;

    if (!token) {
      throw new Error(
        "Authentication token not found.",
      );
    }


    const baseURL =
      api.defaults.baseURL;

    if (!baseURL) {
      throw new Error(
        "API base URL is not configured.",
      );
    }


    const response = await fetch(
      `${baseURL}/chat/stream`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify(data),
      },
    );


    if (!response.ok) {

      let errorMessage =
        `Chat request failed: ${response.status}`;

      try {

        const errorData =
          await response.json();

        if (errorData?.detail) {
          errorMessage =
            errorData.detail;
        }

      } catch {
        // Ignore JSON parsing errors
      }

      throw new Error(
        errorMessage,
      );
    }


    if (!response.body) {
      throw new Error(
        "Streaming is not supported.",
      );
    }


    // ------------------------------------------------------
    // Get session ID
    // ------------------------------------------------------

    const sessionHeader =
      response.headers.get(
        "X-Session-Id",
      );

    const returnedSessionId =
      sessionHeader
        ? Number(sessionHeader)
        : data.session_id ?? 0;


    // ------------------------------------------------------
    // Read stream
    // ------------------------------------------------------

    const reader =
      response.body.getReader();

    const decoder =
      new TextDecoder();


    while (true) {

      const {
        value,
        done,
      } = await reader.read();


      if (done) {
        break;
      }


      const chunk =
        decoder.decode(
          value,
          {
            stream: true,
          },
        );


      if (chunk) {
        onToken(chunk);
      }
    }


    return returnedSessionId;
  }
}


export default new ChatService();