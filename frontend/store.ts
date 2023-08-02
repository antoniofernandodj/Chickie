// store.js

import { configureStore } from '@reduxjs/toolkit';
import authReducer from './reducers/storeToken';

export const store = configureStore({
  reducer: {
    tokenStore: authReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>
// type RootState = {
//   tokenStore: TokenState;
// }
export type AppDispatch = typeof store.dispatch
