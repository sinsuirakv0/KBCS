# 00bb9ddc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb9d98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0017.md#compare-9baa5ec5ac0cc5b1bb467db5d26833f9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb9ddc",
  "name": "FUN_00bb9ddc",
  "size": 556,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ff3a976dd27eae414ee67d614681cbcb886f45d65e8d2aaedacb295bc790480",
  "source_text_sha256": "0ff3a976dd27eae414ee67d614681cbcb886f45d65e8d2aaedacb295bc790480"
}
~~~

## 呼び出し元

- [00bb81a8](../00bb8/00bb81a8.md)
- [00bb81d8](../00bb8/00bb81d8.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1930](../00be1/00be1930.md)

## 疑似コード / UTF-8 4099 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00bb9ddc(undefined8 *param_1)

{
  byte bVar1;
  long lVar2;
  
  if ((*(byte *)(param_1 + 0x82) & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x7f);
  }
  else {
    _ZdlPv((void *)param_1[0x84]);
    bVar1 = *(byte *)(param_1 + 0x7f);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x7c);
  }
  else {
    _ZdlPv((void *)param_1[0x81]);
    bVar1 = *(byte *)(param_1 + 0x7c);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x79);
  }
  else {
                    /* try { // try from 00bb9f04 to 00cb9f0b has its CatchHandler @ 00bba558 */
    _ZdlPv((void *)param_1[0x7e]);
    bVar1 = *(byte *)(param_1 + 0x79);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x76);
  }
  else {
    _ZdlPv((void *)param_1[0x7b]);
    bVar1 = *(byte *)(param_1 + 0x76);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x73);
  }
  else {
    _ZdlPv((void *)param_1[0x78]);
    bVar1 = *(byte *)(param_1 + 0x73);
  }
  if ((bVar1 & 1) != 0) {
                    /* try { // try from 00bb9e24 to 00cb9e2f has its CatchHandler @ 00bbaad0 */
    _ZdlPv((void *)param_1[0x75]);
  }
  lVar2 = 0x240;
  do {
    if ((*(byte *)((long)param_1 + lVar2 + 0x140) & 1) != 0) {
      _ZdlPv(*(void **)((long)param_1 + lVar2 + 0x150));
    }
                    /* try { // try from 00bb9e30 to 00cb9e3f has its CatchHandler @ 00bbaabc */
    lVar2 = lVar2 + -0x18;
  } while (lVar2 != 0);
  if ((*(byte *)(param_1 + 0x28) & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x25);
  }
  else {
    _ZdlPv((void *)param_1[0x2a]);
    bVar1 = *(byte *)(param_1 + 0x25);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x22);
  }
  else {
    _ZdlPv((void *)param_1[0x27]);
    bVar1 = *(byte *)(param_1 + 0x22);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x1f);
  }
  else {
                    /* try { // try from 00bb9f54 to 00cb9f5f has its CatchHandler @ 00bba554 */
    _ZdlPv((void *)param_1[0x24]);
    bVar1 = *(byte *)(param_1 + 0x1f);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x1c);
  }
  else {
                    /* try { // try from 00bb9f64 to 00cb9f73 has its CatchHandler @ 00bba540 */
    _ZdlPv((void *)param_1[0x21]);
    bVar1 = *(byte *)(param_1 + 0x1c);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x19);
  }
  else {
                    /* try { // try from 00bb9f74 to 00cb9f87 has its CatchHandler @ 00bba528 */
    _ZdlPv((void *)param_1[0x1e]);
    bVar1 = *(byte *)(param_1 + 0x19);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x16);
  }
  else {
    _ZdlPv((void *)param_1[0x1b]);
    bVar1 = *(byte *)(param_1 + 0x16);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x13);
  }
  else {
    _ZdlPv((void *)param_1[0x18]);
    bVar1 = *(byte *)(param_1 + 0x13);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0x10);
  }
  else {
    _ZdlPv((void *)param_1[0x15]);
    bVar1 = *(byte *)(param_1 + 0x10);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0xd);
  }
  else {
    _ZdlPv((void *)param_1[0x12]);
    bVar1 = *(byte *)(param_1 + 0xd);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 10);
  }
  else {
    _ZdlPv((void *)param_1[0xf]);
    bVar1 = *(byte *)(param_1 + 10);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 7);
  }
  else {
    _ZdlPv((void *)param_1[0xc]);
    bVar1 = *(byte *)(param_1 + 7);
  }
  if ((bVar1 & 1) == 0) {
                    /* try { // try from 00bb9eb0 to 00cb9ebb has its CatchHandler @ 00bbaaec */
    bVar1 = *(byte *)(param_1 + 4);
  }
  else {
    _ZdlPv((void *)param_1[9]);
    bVar1 = *(byte *)(param_1 + 4);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 1);
  }
  else {
    _ZdlPv((void *)param_1[6]);
    bVar1 = *(byte *)(param_1 + 1);
  }
  if ((bVar1 & 1) != 0) {
                    /* try { // try from 00bb9ec0 to 00cb9ecf has its CatchHandler @ 00bbaad8 */
    _ZdlPv((void *)param_1[3]);
  }
  freelocale((__locale_t)*param_1);
  return;
}

~~~
