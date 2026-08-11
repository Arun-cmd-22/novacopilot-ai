"use client";

import { Bell, Search } from "lucide-react";
import { useAuthStore } from "@/store/auth.store";

export default function Header() {
  const user = useAuthStore((state) => state.user);

  const name = user?.full_name || "User";
  const initial = name.charAt(0).toUpperCase();

  return (
    <header className="flex h-20 items-center justify-between border-b border-white/10 bg-slate-950/80 px-8 backdrop-blur-xl">
      <div>
        <h1 className="text-lg font-semibold text-white">
          Dashboard
        </h1>

        <p className="text-xs text-slate-500">
          Welcome back, {name}
        </p>
      </div>

      <div className="flex items-center gap-4">
        <div className="hidden items-center gap-2 rounded-xl border border-white/10 bg-white/5 px-4 py-2 md:flex">
          <Search size={16} className="text-slate-500" />

          <input
            placeholder="Search..."
            className="w-40 bg-transparent text-sm text-white outline-none placeholder:text-slate-600"
          />
        </div>

        <button
          type="button"
          className="rounded-xl border border-white/10 p-2.5 text-slate-400 transition hover:bg-white/10 hover:text-white"
        >
          <Bell size={18} />
        </button>

        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-violet-600 text-sm font-semibold text-white">
          {initial}
        </div>
      </div>
    </header>
  );
}