"use client";

import { useRouter } from "next/navigation";

import AuthService from "@/services/auth";

import { LoginRequest } from "@/types/auth";

import { useAuthStore } from "@/store/authStore";

export function useAuth() {

    const router = useRouter();

    const {
        setUser,
        setTokens,
        clearAuth,
    } = useAuthStore();

    const login = async (
        data: LoginRequest,
    ) => {

        try {

            const result =
                await AuthService.login(data);

            AuthService.saveTokens(
                result.access_token,
                result.refresh_token,
            );

            setTokens(
                result.access_token,
                result.refresh_token,
            );

            const user =
                await AuthService.getCurrentUser();

            setUser(user);

            router.push("/dashboard");

        }

        catch (error) {

            throw error;

        }

    };

    const logout = () => {

        AuthService.logout();

        clearAuth();

        router.push("/login");

    };

    return {

        login,

        logout,

    };

}