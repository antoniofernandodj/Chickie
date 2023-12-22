import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface TokenState {
  value: string | null;
}


const initialState: TokenState = {
  value: null,
};

export const tokenSlice = createSlice({
  name: 'tokenStore',
  initialState,
  reducers: {
    storeToken: (state, action: PayloadAction<string>) => {
      state.value = action.payload;
    },
    clearToken: (state) => {
      state.value = null;
    },
  },
});

export const { storeToken, clearToken } = tokenSlice.actions
export default tokenSlice.reducer