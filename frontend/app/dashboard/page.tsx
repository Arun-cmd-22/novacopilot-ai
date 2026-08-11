"use client";

import {
  Bot,
  MessageSquare,
  Users,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

import StatCard from "@/components/ui/StatCard";
import { useAuthStore } from "@/store/auth.store";

export default function DashboardPage() {
  const user = useAuthStore((state) => state.user);
  const name = user?.full_name || "User";

  return (
    <div className="min-h-full bg-slate-950 p-8">
      <div className="mb-8">
        <div className="flex items-center gap-2 text-sm text-violet-400">
          <Sparkles size={16} />
          NovaCopilot AI
        </div>

        <h1 className="mt-2 text-3xl font-bold text-white">
          Welcome, {name}
        </h1>

        <p className="mt-2 text-slate-400">
          Your intelligent workspace is ready.
        </p>
      </div>

      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="AI Conversations"
          value="0"
          description="Total conversations"
          icon={MessageSquare}
        />

        <StatCard
          title="AI Requests"
          value="0"
          description="Requests processed"
          icon={Bot}
        />

        <StatCard
          title="Users"
          value="0"
          description="Registered users"
          icon={Users}
        />

        <StatCard
          title="Permissions"
          value="0"
          description="Available permissions"
          icon={ShieldCheck}
        />
      </div>

      <div className="mt-8 rounded-3xl border border-white/10 bg-gradient-to-br from-violet-600/20 via-white/[0.04] to-transparent p-8">
        <div className="flex items-center gap-4">
          <div className="rounded-2xl bg-violet-500/20 p-4 text-violet-300">
            <Bot size={28} />
          </div>

          <div>
            <h2 className="text-xl font-semibold text-white">
              AI Workspace
            </h2>

            <p className="mt-1 text-sm text-slate-400">
              Start a conversation with NovaCopilot.
            </p>
          </div>
        </div>

        <button className="mt-6 rounded-xl bg-violet-600 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500">
          Start AI Chat
        </button>
      </div>
    </div>
  );
}