import "./globals.css";
import { GeistSans } from "geist/font/sans";
import { Providers } from "./providers";

export const metadata = {
  title: "Apollo",
  description: "Generate and visualize educational videos",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={GeistSans.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
