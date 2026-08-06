"use client";

import { useState } from "react";

import { useForm } from "react-hook-form";

import { zodResolver } from "@hookform/resolvers/zod";

import { Eye, EyeOff } from "lucide-react";

import { toast } from "sonner";

import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";
import Input from "@/components/ui/Input";

import { loginSchema, LoginFormData } from "@/schemas/auth";

import { useAuth } from "@/hooks/useAuth";

export default function LoginForm() {

    const { login } = useAuth();

    const [showPassword, setShowPassword] = useState(false);

    const [loading, setLoading] = useState(false);

    const {

        register,

        handleSubmit,

        formState: { errors },

    } = useForm<LoginFormData>({

        resolver: zodResolver(loginSchema),

        defaultValues: {

            username: "",

            password: "",

        },

    });

    const onSubmit = async (

        data: LoginFormData,

    ) => {

        try {

            setLoading(true);

            await login(data);

            toast.success(

                "Login successful.",

            );

        }

        catch (error) {

            toast.error(

                "Invalid username or password.",

            );

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="flex min-h-screen items-center justify-center bg-gray-100 p-4">

            <Card className="w-full max-w-md">

                <div className="mb-6 text-center">

                    <h1 className="text-3xl font-bold">

                        NovaCopilotAI

                    </h1>

                    <p className="mt-2 text-gray-500">

                        Sign in to continue

                    </p>

                </div>

                <form

                    onSubmit={handleSubmit(onSubmit)}

                    className="space-y-5"

                >

                    <Input

                        label="Username"

                        placeholder="Enter username"

                        {...register("username")}

                        error={errors.username?.message}

                    />

                    <div className="relative">

                        <Input

                            label="Password"

                            type={

                                showPassword

                                    ? "text"

                                    : "password"

                            }

                            placeholder="Enter password"

                            {...register("password")}

                            error={errors.password?.message}

                        />

                        <button

                            type="button"

                            onClick={() =>

                                setShowPassword(

                                    !showPassword,

                                )

                            }

                            className="absolute right-3 top-11"

                        >

                            {

                                showPassword

                                    ? <EyeOff size={18} />

                                    : <Eye size={18} />

                            }

                        </button>

                    </div>

                    <Button

                        type="submit"

                        loading={loading}

                    >

                        Login

                    </Button>

                </form>

            </Card>

        </div>

    );

}