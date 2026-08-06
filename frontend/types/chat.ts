export interface ChatRequest {

    session_id?: number | null;

    message: string;
}

export interface ChatResponse {

    session_id: number;

    response: string;

    response_time: number;
}

export interface ChatSession {

    id: number;

    title: string;

    ai_model_id: number;

    user_id: number;

    created_at: string;
}

export interface ChatMessage {

    id: number;

    session_id: number;

    role: "user" | "assistant";

    message: string;

    response_time?: number;

    created_at: string;
}