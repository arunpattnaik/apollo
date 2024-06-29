"use client";
import { NextUIProvider } from "@nextui-org/react";

export function Providers({ children, ...props }: any) {
  return <NextUIProvider {...props}>{children}</NextUIProvider>;
}
