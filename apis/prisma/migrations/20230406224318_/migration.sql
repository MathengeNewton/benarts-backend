/*
  Warnings:

  - A unique constraint covering the columns `[phone]` on the table `sales_reps` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `phone` to the `sales_reps` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "sales_reps" ADD COLUMN     "phone" TEXT NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "sales_reps_phone_key" ON "sales_reps"("phone");
