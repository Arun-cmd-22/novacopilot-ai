import api from "./api";

import {
    LoginRequest,
    LoginResponse,
    User,
} from "@/types/auth";


class AuthService {

    /**
     * Login User
     */
    async login(
        data: LoginRequest,
    ): Promise<LoginResponse> {

        const response = await api.post(
            "/auth/login",
            data,
        );

        return response.data;
    }

    /**
     * Register User
     */
    async register(
        data: unknown,
    ) {

        const response = await api.post(
            "/auth/register",
            data,
        );

        return response.data;
    }

    /**
     * Get Logged-in User
     */
    async getCurrentUser(): Promise<User> {

        const response = await api.get(
            "/users/me",
        );

        return response.data;
    }

    /**
     * Refresh Access Token
     */
    async refreshToken(
        refreshToken: string,
    ): Promise<LoginResponse> {

        const response = await api.post(
            "/auth/refresh-token",
            {
                refresh_token: refreshToken,
            },
        );

        return response.data;
    }

    /**
     * Save Tokens
     */
    saveTokens(
        accessToken: string,
        refreshToken: string,
    ): void {

        localStorage.setItem(
            "access_token",
            accessToken,
        );

        localStorage.setItem(
            "refresh_token",
            refreshToken,
        );
    }

    /**
     * Get Access Token
     */
    getAccessToken(): string | null {

        return localStorage.getItem(
            "access_token",
        );
    }

    /**
     * Get Refresh Token
     */
    getRefreshToken(): string | null {

        return localStorage.getItem(
            "refresh_token",
        );
    }

    /**
     * Check Login Status
     */
    isAuthenticated(): boolean {

        return !!this.getAccessToken();
    }

    /**
     * Logout User
     */
    logout(): void {

        localStorage.removeItem(
            "access_token",
        );

        localStorage.removeItem(
            "refresh_token",
        );

        window.location.href = "/login";
    }

}

export default new AuthService();