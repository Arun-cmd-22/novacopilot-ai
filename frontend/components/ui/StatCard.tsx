import { LucideIcon } from "lucide-react";

interface StatCardProps {
  title: string;
  value: string;
  description: string;
  icon: LucideIcon;
}

export default function StatCard({ title, value, description, icon: Icon }: StatCardProps) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/[0.04] p-6 transition hover:border-violet-500/30 hover:bg-white/[0.06]">
      <div className="flex items-center justify-between">
        <div className="rounded-xl bg-violet-500/10 p-3 text-violet-400">
          <Icon size={20} />
        </div>
      </div>

      <p className="mt-5 text-sm text-slate-400">{title}</p>
      <p className="mt-1 text-3xl font-bold text-white">{value}</p>
      <p className="mt-2 text-xs text-slate-500">{description}</p>
    </div>
  );
}