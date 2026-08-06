import api from "./api";

export interface ChatRequest {
    session_id?: number | null;
    message: string;
}

export interface ChatResponse {
    session_id: number;
    response: string;
    response_time: number;
}

class ChatService {

    async sendMessage(
        data: ChatRequest,
    ): Promise<ChatResponse> {

        const response = await api.post(
            "/chat",
            data,
        );

        return response.data;
    }

    async streamMessage(
        data: ChatRequest,
    ) {

        const token = localStorage.getItem(
            "access_token",
        );

        return fetch(
            `${process.env.NEXT_PUBLIC_API_URL}/chat/stream`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(data),
            },
        );
    }

    async getSessions() {

        const response = await api.get(
            "/chat-session",
        );

        return response.data;
    }

    async getMessages(
        sessionId: number,
    ) {

        const response = await api.get(
            `/message/${sessionId}`,
        );

        return response.data;
    }

    async deleteSession(
        sessionId: number,
    ) {

        const response = await api.delete(
            `/chat-session/${sessionId}`,
        );

        return response.data;
    }
}

export default new ChatService();