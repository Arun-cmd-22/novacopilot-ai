import { create } from "zustand";

import { User } from "@/types/auth";

interface AuthState {

    user: User | null;

    accessToken: string | null;

    refreshToken: string | null;

    isAuthenticated: boolean;

    setUser: (
        user: User,
    ) => void;

    setTokens: (
        accessToken: string,
        refreshToken: string,
    ) => void;

    clearAuth: () => void;

}

export const useAuthStore = create<AuthState>((set) => ({

    user: null,

    accessToken: null,

    refreshToken: null,

    isAuthenticated: false,

    setUser: (user) =>
        set({
            user,
        }),

    setTokens: (
        accessToken,
        refreshToken,
    ) =>
        set({
            accessToken,
            refreshToken,
            isAuthenticated: true,
        }),

    clearAuth: () =>
        set({
            user: null,
            accessToken: null,
            refreshToken: null,
            isAuthenticated: false,
        }),

}));