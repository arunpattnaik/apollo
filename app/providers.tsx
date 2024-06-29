"use client";
import { NextUIProvider } from "@nextui-org/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

export function Providers({ children, ...props }: any) {
  return (
    <QueryClientProvider client={queryClient}>
      <NextUIProvider {...props}>{children}</NextUIProvider>
    </QueryClientProvider>
  );
}
