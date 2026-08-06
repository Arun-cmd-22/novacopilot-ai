import api from "./api";

export interface LoginRequest {
    username: string;
    password: string;
}

export interface LoginResponse {
    access_token: string;
    refresh_token: string;
    token_type: string;
}

class AuthService {

    async login(
        data: LoginRequest,
    ): Promise<LoginResponse> {

        const response = await api.post(
            "/auth/login",
            data,
        );

        return response.data;
    }

    async register(
        data: unknown,
    ) {

        const response = await api.post(
            "/auth/register",
            data,
        );

        return response.data;
    }

    async getCurrentUser() {

        const response = await api.get(
            "/users/me",
        );

        return response.data;
    }

    logout() {

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