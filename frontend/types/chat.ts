export interface ChatRequest {
  session_id: number | null;
  message: string;
}


export interface ChatResponse {
  session_id: number;
  response: string;
  response_time: number;
}


export interface ChatMessage {
  id: number;
  session_id: number;
  role: "user" | "assistant";
  content: string;
  created_at: string;
}