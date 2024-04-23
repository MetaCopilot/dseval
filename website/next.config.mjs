/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {unoptimized: true},
    output: 'export',
    distDir: '../_site',
    basePath: '/dseval',
};

export default nextConfig;
