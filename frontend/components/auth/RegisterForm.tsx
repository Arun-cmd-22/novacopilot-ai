"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Mail, Phone, User, Sparkles } from "lucide-react";

import AuthService from "@/services/auth.service";
import Input from "@/components/ui/Input";
import PasswordInput from "@/components/ui/PasswordInput";
import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";

import {
  registerSchema,
  type RegisterFormData,
} from "@/schemas/register.schema";

export default function RegisterForm() {
  const router = useRouter();
  const [serverError, setServerError] = useState("");
  const [success, setSuccess] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      full_name: "",
      email: "",
      mobile: "",
      password: "",
    },
  });

  const onSubmit = async (data: RegisterFormData) => {
    setServerError("");
    setSuccess("");

    try {
      const response = await AuthService.register(data);

      if (!response.success) {
        setServerError(response.message);
        return;
      }

      setSuccess(response.message);

      setTimeout(() => {
        router.push("/login");
      }, 1000);
    } catch (error: any) {
      setServerError(
        error?.response?.data?.detail ||
          "Unable to connect to the server.",
      );
    }
  };

  return (
    <Card>
      <div className="mb-5 text-center">
        <div className="mx-auto mb-3 flex h-12 w-12 items-center justify-center rounded-xl bg-violet-600/20 text-violet-400">
          <Sparkles size={24} />
        </div>

        <h1 className="text-2xl font-bold text-white">
          Create account
        </h1>

        <p className="mt-1 text-xs text-slate-400">
          Join your NovaCopilot workspace
        </p>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-3">
        <div>
          <Input
            {...register("full_name")}
            label="Full Name"
            icon={User}
            placeholder="Enter your full name"
          />

          {errors.full_name && (
            <p className="mt-1 text-xs text-red-400">
              {errors.full_name.message}
            </p>
          )}
        </div>

        <div>
          <Input
            {...register("email")}
            label="Email"
            type="email"
            icon={Mail}
            placeholder="Enter your email"
          />

          {errors.email && (
            <p className="mt-1 text-xs text-red-400">
              {errors.email.message}
            </p>
          )}
        </div>

        <div>
          <Input
            {...register("mobile")}
            label="Mobile"
            type="tel"
            icon={Phone}
            placeholder="Enter your mobile number"
          />

          {errors.mobile && (
            <p className="mt-1 text-xs text-red-400">
              {errors.mobile.message}
            </p>
          )}
        </div>

        <div>
          <PasswordInput
            {...register("password")}
            label="Password"
            placeholder="Create a password"
          />

          {errors.password && (
            <p className="mt-1 text-xs text-red-400">
              {errors.password.message}
            </p>
          )}
        </div>

        {serverError && (
          <div className="rounded-lg border border-red-500/20 bg-red-500/10 p-2.5 text-xs text-red-400">
            {serverError}
          </div>
        )}

        {success && (
          <div className="rounded-lg border border-emerald-500/20 bg-emerald-500/10 p-2.5 text-xs text-emerald-400">
            {success}
          </div>
        )}

        <Button type="submit" loading={isSubmitting}>
          Create account
        </Button>
      </form>

      <p className="mt-4 text-center text-xs text-slate-500">
        Already have an account?{" "}
        <button
          type="button"
          onClick={() => router.push("/login")}
          className="font-medium text-violet-400 hover:text-violet-300"
        >
          Sign in
        </button>
      </p>
    </Card>
  );
}