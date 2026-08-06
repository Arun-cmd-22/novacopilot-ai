import { create } from "zustand";

import {
    ChatMessage,
} from "@/types/chat";

interface ChatState {

    sessionId: number | null;

    messages: ChatMessage[];

    loading: boolean;

    setSessionId: (
        sessionId: number,
    ) => void;

    setMessages: (
        messages: ChatMessage[],
    ) => void;

    addMessage: (
        message: ChatMessage,
    ) => void;

    clearMessages: () => void;

    setLoading: (
        loading: boolean,
    ) => void;

}

export const useChatStore =
create<ChatState>((set) => ({

    sessionId: null,

    messages: [],

    loading: false,

    setSessionId: (sessionId) =>
        set({
            sessionId,
        }),

    setMessages: (messages) =>
        set({
            messages,
        }),

    addMessage: (message) =>
        set((state) => ({
            messages: [
                ...state.messages,
                message,
            ],
        })),

    clearMessages: () =>
        set({
            messages: [],
            sessionId: null,
        }),

    setLoading: (loading) =>
        set({
            loading,
        }),

}));