"use client";

import {
  FormEvent,
  useEffect,
  useRef,
  useState,
} from "react";

import {
  ArrowLeft,
  ArrowUp,
  MessageSquare,
  Paperclip,
  Search,
  Sparkles,
} from "lucide-react";

import { useRouter } from "next/navigation";

import ChatService from "@/services/chat.service";

import { useAuthStore } from "@/store/auth.store";

import type { ChatMessage } from "@/types/chat";

export default function ChatPage() {
  const router = useRouter();

  // ========================================================
  // AUTH
  // ========================================================

  const user = useAuthStore(
    (state) => state.user,
  );

  // ========================================================
  // CHAT STATE
  // ========================================================

  const [messages, setMessages] = useState<
    ChatMessage[]
  >([]);

  const [message, setMessage] = useState("");

  const [sessionId, setSessionId] = useState<
    number | null
  >(null);

  const [loading, setLoading] = useState(false);

  const [search, setSearch] = useState("");

  // ========================================================
  // MESSAGE SCROLL
  // ========================================================

  const messagesEndRef =
    useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "auto",
      block: "end",
    });
  }, [messages, loading]);

  // ========================================================
  // USER NAME
  // ========================================================

  const fullName =
    user?.full_name ||
    user?.email ||
    "User";

  // ========================================================
  // SEND MESSAGE
  // ========================================================

  const sendMessage = async (
    event?: FormEvent,
  ) => {
    event?.preventDefault();

    const text = message.trim();

    if (!text || loading) {
      return;
    }

    // ------------------------------------------------------
    // User message
    // ------------------------------------------------------

    const userMessage: ChatMessage = {
      id: Date.now(),
      session_id: sessionId ?? 0,
      role: "user",
      content: text,
      created_at:
        new Date().toISOString(),
    };

    setMessages((current) => [
      ...current,
      userMessage,
    ]);

    setMessage("");
    setLoading(true);

    // ------------------------------------------------------
    // Temporary AI message
    // ------------------------------------------------------

    const assistantId =
      Date.now() + 1;

    const assistantMessage: ChatMessage = {
      id: assistantId,
      session_id: sessionId ?? 0,
      role: "assistant",
      content: "",
      created_at:
        new Date().toISOString(),
    };

    setMessages((current) => [
      ...current,
      assistantMessage,
    ]);

    try {
      const returnedSessionId =
        await ChatService.streamMessage(
          {
            session_id: sessionId,
            message: text,
          },
          (token) => {
            setMessages(
              (current) =>
                current.map(
                  (item) =>
                    item.id === assistantId
                      ? {
                          ...item,
                          content:
                            item.content +
                            token,
                        }
                      : item,
                ),
            );
          },
        );

      if (returnedSessionId) {
        setSessionId(
          returnedSessionId,
        );
      }
    } catch (error) {
      console.error(
        "Chat error:",
        error,
      );

      setMessages(
        (current) =>
          current.map(
            (item) =>
              item.id === assistantId
                ? {
                    ...item,
                    content:
                      "Sorry, something went wrong. Please try again.",
                  }
                : item,
          ),
      );
    } finally {
      setLoading(false);
    }
  };

  // ========================================================
  // NEW CHAT
  // ========================================================

  const newChat = () => {
    setMessages([]);
    setSessionId(null);
    setMessage("");
  };

  // ========================================================
  // KEYBOARD
  // ========================================================

  const handleKeyDown = (
    event: React.KeyboardEvent<HTMLTextAreaElement>,
  ) => {
    if (
      event.key === "Enter" &&
      !event.shiftKey
    ) {
      event.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex h-screen min-h-0 overflow-hidden bg-[#080808] text-white">

      {/* ==================================================
          SIDEBAR
      ================================================== */}

      <aside className="flex w-[310px] shrink-0 flex-col border-r border-white/10 bg-[#0b0b0b]">

        {/* ------------------------------------------------
            LOGO
        ------------------------------------------------ */}

        <div className="px-5 pb-5 pt-6">
          <div className="flex items-center gap-3">

            <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-violet-600 text-white shadow-lg shadow-violet-900/20">
              <Sparkles size={22} />
            </div>

            <div>
              <h1 className="text-lg font-semibold">
                NovaCopilot
              </h1>

              <p className="text-xs text-slate-500">
                AI Workspace
              </p>
            </div>

          </div>
        </div>

        {/* ------------------------------------------------
            SEARCH
        ------------------------------------------------ */}

        <div className="px-4">
          <div className="flex items-center gap-3 rounded-xl border border-white/10 bg-white/[0.03] px-3 py-3">

            <Search
              size={18}
              className="text-slate-500"
            />

            <input
              value={search}
              onChange={(event) =>
                setSearch(
                  event.target.value,
                )
              }
              placeholder="Search chats"
              className="w-full bg-transparent text-sm text-white outline-none placeholder:text-slate-600"
            />

          </div>
        </div>

        {/* ------------------------------------------------
            RECENT CHATS
        ------------------------------------------------ */}

        <div className="mt-6 px-4">

          <p className="mb-3 px-2 text-xs font-medium uppercase tracking-wider text-slate-600">
            Recent Chats
          </p>

          {messages.length > 0 ? (
            <button
              type="button"
              className="flex w-full items-center gap-3 rounded-xl bg-white/[0.05] px-3 py-3 text-left transition hover:bg-white/[0.08]"
            >

              <MessageSquare
                size={18}
                className="text-slate-400"
              />

              <span className="truncate text-sm text-slate-300">
                {messages[0]?.content ||
                  "Current conversation"}
              </span>

            </button>
          ) : (
            <div className="px-2 text-sm text-slate-600">
              No conversations yet
            </div>
          )}

        </div>

        {/* ------------------------------------------------
            USER
        ------------------------------------------------ */}

        <div className="mt-auto border-t border-white/10 p-4">

          <div className="flex items-center gap-3">

            <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-violet-600 text-sm font-semibold">

              {fullName
                .charAt(0)
                .toUpperCase()}

            </div>

            <div className="min-w-0">

              <p className="truncate text-sm font-medium text-white">
                {fullName}
              </p>

              <p className="truncate text-xs text-slate-500">
                {user?.email}
              </p>

            </div>

          </div>

        </div>

      </aside>

      {/* ==================================================
          MAIN
      ================================================== */}

      <main className="flex min-h-0 min-w-0 flex-1 flex-col">

        {/* ------------------------------------------------
            HEADER
        ------------------------------------------------ */}

        <header className="flex h-[76px] shrink-0 items-center justify-between border-b border-white/10 px-8">

          <div className="flex items-center gap-4">

            <button
              type="button"
              onClick={() =>
                router.push(
                  "/dashboard",
                )
              }
              className="flex items-center gap-2 text-sm text-slate-400 transition hover:text-white"
            >

              <ArrowLeft size={20} />

              <span>
                Dashboard
              </span>

            </button>

            <div className="h-5 w-px bg-white/10" />

            <div className="flex items-center gap-2">

              <Sparkles
                size={19}
                className="text-violet-400"
              />

              <span className="font-medium">
                NovaCopilot
              </span>

            </div>

          </div>

          <button
            type="button"
            onClick={newChat}
            className="rounded-lg border border-white/10 px-4 py-2 text-sm text-slate-400 transition hover:bg-white/5 hover:text-white"
          >
            New chat
          </button>

        </header>

        {/* ------------------------------------------------
            CHAT CONTENT
        ------------------------------------------------ */}

        <div className="relative flex min-h-0 flex-1 flex-col">

          {/* =================================================
              EMPTY CHAT
          ================================================= */}

          {messages.length === 0 ? (

            <div className="flex min-h-0 flex-1 items-center justify-center px-6">

              <div className="w-full max-w-[820px]">

                <div className="mb-8 text-center">

                  <div className="mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-violet-600/15 text-violet-400">

                    <Sparkles size={30} />

                  </div>

                  <h2 className="text-4xl font-semibold tracking-tight">

                    How can I help,{" "}

                    <span className="text-violet-400">
                      {fullName}
                    </span>
                    ?

                  </h2>

                </div>

                {/* CENTER INPUT */}

                <ChatInput
                  message={message}
                  setMessage={setMessage}
                  loading={loading}
                  onSubmit={sendMessage}
                  onKeyDown={handleKeyDown}
                />

              </div>

            </div>

          ) : (

            <>
              {/* =================================================
                  MESSAGES
              ================================================= */}

              <div className="min-h-0 flex-1 overflow-y-auto">

                <div className="mx-auto w-full max-w-[900px] px-6 py-10">

                  {messages.map(
                    (item) => {

                      const isUser =
                        item.role ===
                        "user";

                      return (

                        <div
                          key={item.id}
                          className={`mb-8 flex ${
                            isUser
                              ? "justify-end"
                              : "justify-start"
                          }`}
                        >

                          {isUser ? (

                            <div className="flex max-w-[75%] items-end gap-3">

                              <div className="rounded-3xl bg-violet-600 px-5 py-3 text-sm leading-7 text-white">

                                {item.content}

                              </div>

                              <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-violet-600 text-xs font-semibold">

                                {fullName
                                  .charAt(0)
                                  .toUpperCase()}

                              </div>

                            </div>

                          ) : (

                            <div className="flex max-w-[85%] items-start gap-4">

                              <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-violet-600/15 text-violet-400">

                                <Sparkles
                                  size={18}
                                />

                              </div>

                              <div className="min-w-0 pt-1">

                                <p className="mb-2 text-xs font-semibold text-violet-400">
                                  NovaCopilot
                                </p>

                                <div className="whitespace-pre-wrap text-[15px] leading-7 text-slate-200">

                                  {item.content}

                                  {loading &&
                                    item.id ===
                                      messages[
                                        messages.length -
                                          1
                                      ]?.id && (

                                      <span className="ml-1 inline-block animate-pulse text-violet-400">
                                        ▋
                                      </span>

                                    )}

                                </div>

                              </div>

                            </div>

                          )}

                        </div>

                      );

                    },
                  )}

                  {/* Scroll target */}

                  <div
                    ref={
                      messagesEndRef
                    }
                  />

                </div>

              </div>

              {/* =================================================
                  BOTTOM INPUT
              ================================================= */}

              <div className="shrink-0 border-t border-white/10 bg-[#080808] px-6 py-5">

                <div className="mx-auto w-full max-w-[900px]">

                  <ChatInput
                    message={message}
                    setMessage={setMessage}
                    loading={loading}
                    onSubmit={sendMessage}
                    onKeyDown={handleKeyDown}
                  />

                </div>

              </div>
            </>

          )}

        </div>

      </main>

    </div>
  );
}


// ============================================================
// CHAT INPUT COMPONENT
// ============================================================

interface ChatInputProps {

  message: string;

  setMessage: (
    value: string,
  ) => void;

  loading: boolean;

  onSubmit: (
    event?: FormEvent,
  ) => void;

  onKeyDown: (
    event: React.KeyboardEvent<HTMLTextAreaElement>,
  ) => void;
}


function ChatInput({
  message,
  setMessage,
  loading,
  onSubmit,
  onKeyDown,
}: ChatInputProps) {

  return (

    <div>

      <form
        onSubmit={onSubmit}
        className="rounded-3xl border border-white/10 bg-[#242424] shadow-2xl shadow-black/30 transition focus-within:border-violet-500/40"
      >

        <textarea
          value={message}
          onChange={(event) =>
            setMessage(
              event.target.value,
            )
          }
          onKeyDown={onKeyDown}
          placeholder="Message NovaCopilot..."
          rows={1}
          disabled={loading}
          className="max-h-48 min-h-[68px] w-full resize-none bg-transparent px-5 pt-5 text-[15px] text-white outline-none placeholder:text-slate-500 disabled:opacity-50"
        />

        <div className="flex items-center justify-between px-4 pb-3">

          <button
            type="button"
            className="flex h-9 w-9 items-center justify-center rounded-full text-slate-400 transition hover:bg-white/10 hover:text-white"
          >

            <Paperclip size={19} />

          </button>

          <button
            type="submit"
            disabled={
              !message.trim() ||
              loading
            }
            className="flex h-10 w-10 items-center justify-center rounded-full bg-white text-black transition hover:bg-slate-200 disabled:cursor-not-allowed disabled:opacity-30"
          >

            {loading ? (

              <span className="h-4 w-4 animate-spin rounded-full border-2 border-black/20 border-t-black" />

            ) : (

              <ArrowUp size={20} />

            )}

          </button>

        </div>

      </form>

      <p className="mt-3 text-center text-[11px] text-slate-600">
        NovaCopilot may generate inaccurate information. Verify important results.
      </p>

    </div>
  );
}