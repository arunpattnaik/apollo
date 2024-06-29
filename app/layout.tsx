import { GeistSans } from "geist/font/sans";
import "./globals.css";

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
      <body className={GeistSans.className}>{children}</body>
    </html>
  );
}
