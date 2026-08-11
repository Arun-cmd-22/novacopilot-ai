import api from "./api";

import type {
  LoginRequest,
  LoginResponse,
  RefreshTokenRequest,
  RefreshTokenResponse,
} from "@/types/auth";

import type {
  RegisterRequest,
  RegisterResponse,
} from "@/types/register";

class AuthService {
  async login(data: LoginRequest): Promise<LoginResponse> {
    const response = await api.post("/login", data);
    return response.data;
  }

  async register(data: RegisterRequest): Promise<RegisterResponse> {
    const response = await api.post("/register", data);
    return response.data;
  }

  async refreshToken(
    data: RefreshTokenRequest,
  ): Promise<RefreshTokenResponse> {
    const response = await api.post("/refresh-token", data);
    return response.data;
  }

  async logout(refreshToken: string) {
    const response = await api.post("/logout", {
      refresh_token: refreshToken,
    });

    return response.data;
  }
}

export default new AuthService();