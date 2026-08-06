export interface LoginRequest {

    username: string;

    password: string;

}

export interface LoginResponse {

    access_token: string;

    refresh_token: string;

    token_type: string;

}

export interface User {

    id: number;

    username: string;

    email: string;

    full_name: string;

    status: boolean;

    role_id: number;

}

export interface RefreshTokenRequest {

    refresh_token: string;

}

export interface JwtPayload {

    sub: string;

    exp: number;

    iat: number;

}