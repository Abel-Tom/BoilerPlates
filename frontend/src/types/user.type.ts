export interface User {
  id: number | string | null,
  username: string | null,
}

export interface Thing {
  id: number | null,
  name: string | null,
  user_name: string | null,
  user: number | null,
}

export type ThingPayload = Pick<Thing, 'name'>;
