// stores.ts
import { writable } from 'svelte/store';

export const loraDataStore = writable<Array<{
  last_name: string;
  latitude: number;
  longitude: number;
  speed: number;
}>>([]);