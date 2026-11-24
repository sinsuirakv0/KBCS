# 00bb9ddc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb9d98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-9baa5ec5ac0cc5b1bb467db5d26833f9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c36824`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-262d100acd33b3a860ec1ab123d76fa4)
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
  "source_text_sha256": "0ff3a976dd27eae414ee67d614681cbcb886f45d65e8d2aaedacb295bc790480",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb9ddc",
        "00bba007"
      ]
    ],
    "bytes_sha256": "702b793c3e52336eb5b268f806ddaceda42c04adf8a16ae6a82487490e3dc7da",
    "instruction_count": 139,
    "instruction_bytes": 556,
    "body_bytes": 556,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bb81a8](../00bb8/00bb81a8.md)
- [00bb81d8](../00bb8/00bb81d8.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1930](../00be1/00be1930.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb9ddc"></a> `00bb9ddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb9de0"></a> `00bb9de0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb9de4"></a> `00bb9de4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb9de8"></a> `00bb9de8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bb9dec"></a> `00bb9dec` | `08 40 50 39` | ldrb w8,[x0, #0x410] | `FALL_THROUGH`
<a id="insn-00bb9df0"></a> `00bb9df0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb9df4"></a> `00bb9df4` | `68 07 00 37` | tbnz w8,#0x0,0x00bb9ee0 | `CONDITIONAL_JUMP`
<a id="insn-00bb9df8"></a> `00bb9df8` | `68 e2 4f 39` | ldrb w8,[x19, #0x3f8] | `FALL_THROUGH`
<a id="insn-00bb9dfc"></a> `00bb9dfc` | `a8 07 00 37` | tbnz w8,#0x0,0x00bb9ef0 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e00"></a> `00bb9e00` | `68 82 4f 39` | ldrb w8,[x19, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bb9e04"></a> `00bb9e04` | `e8 07 00 37` | tbnz w8,#0x0,0x00bb9f00 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e08"></a> `00bb9e08` | `68 22 4f 39` | ldrb w8,[x19, #0x3c8] | `FALL_THROUGH`
<a id="insn-00bb9e0c"></a> `00bb9e0c` | `28 08 00 37` | tbnz w8,#0x0,0x00bb9f10 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e10"></a> `00bb9e10` | `68 c2 4e 39` | ldrb w8,[x19, #0x3b0] | `FALL_THROUGH`
<a id="insn-00bb9e14"></a> `00bb9e14` | `68 08 00 37` | tbnz w8,#0x0,0x00bb9f20 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e18"></a> `00bb9e18` | `68 62 4e 39` | ldrb w8,[x19, #0x398] | `FALL_THROUGH`
<a id="insn-00bb9e1c"></a> `00bb9e1c` | `68 00 00 36` | tbz w8,#0x0,0x00bb9e28 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e20"></a> `00bb9e20` | `60 d6 41 f9` | ldr x0,[x19, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bb9e24"></a> `00bb9e24` | `8f 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9e28"></a> `00bb9e28` | `14 48 80 52` | mov w20,#0x240 | `FALL_THROUGH`
<a id="insn-00bb9e2c"></a> `00bb9e2c` | `03 00 00 14` | b 0x00bb9e38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb9e30"></a> `00bb9e30` | `94 62 00 f1` | subs x20,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bb9e34"></a> `00bb9e34` | `e0 00 00 54` | b.eq 0x00bb9e50 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e38"></a> `00bb9e38` | `68 02 14 8b` | add x8,x19,x20 | `FALL_THROUGH`
<a id="insn-00bb9e3c"></a> `00bb9e3c` | `09 01 45 39` | ldrb w9,[x8, #0x140] | `FALL_THROUGH`
<a id="insn-00bb9e40"></a> `00bb9e40` | `89 ff 07 36` | tbz w9,#0x0,0x00bb9e30 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e44"></a> `00bb9e44` | `00 a9 40 f9` | ldr x0,[x8, #0x150] | `FALL_THROUGH`
<a id="insn-00bb9e48"></a> `00bb9e48` | `86 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9e4c"></a> `00bb9e4c` | `f9 ff ff 17` | b 0x00bb9e30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb9e50"></a> `00bb9e50` | `68 02 45 39` | ldrb w8,[x19, #0x140] | `FALL_THROUGH`
<a id="insn-00bb9e54"></a> `00bb9e54` | `08 07 00 37` | tbnz w8,#0x0,0x00bb9f34 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e58"></a> `00bb9e58` | `68 a2 44 39` | ldrb w8,[x19, #0x128] | `FALL_THROUGH`
<a id="insn-00bb9e5c"></a> `00bb9e5c` | `48 07 00 37` | tbnz w8,#0x0,0x00bb9f44 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e60"></a> `00bb9e60` | `68 42 44 39` | ldrb w8,[x19, #0x110] | `FALL_THROUGH`
<a id="insn-00bb9e64"></a> `00bb9e64` | `88 07 00 37` | tbnz w8,#0x0,0x00bb9f54 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e68"></a> `00bb9e68` | `68 e2 43 39` | ldrb w8,[x19, #0xf8] | `FALL_THROUGH`
<a id="insn-00bb9e6c"></a> `00bb9e6c` | `c8 07 00 37` | tbnz w8,#0x0,0x00bb9f64 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e70"></a> `00bb9e70` | `68 82 43 39` | ldrb w8,[x19, #0xe0] | `FALL_THROUGH`
<a id="insn-00bb9e74"></a> `00bb9e74` | `08 08 00 37` | tbnz w8,#0x0,0x00bb9f74 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e78"></a> `00bb9e78` | `68 22 43 39` | ldrb w8,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-00bb9e7c"></a> `00bb9e7c` | `48 08 00 37` | tbnz w8,#0x0,0x00bb9f84 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e80"></a> `00bb9e80` | `68 c2 42 39` | ldrb w8,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-00bb9e84"></a> `00bb9e84` | `88 08 00 37` | tbnz w8,#0x0,0x00bb9f94 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e88"></a> `00bb9e88` | `68 62 42 39` | ldrb w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bb9e8c"></a> `00bb9e8c` | `c8 08 00 37` | tbnz w8,#0x0,0x00bb9fa4 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e90"></a> `00bb9e90` | `68 02 42 39` | ldrb w8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bb9e94"></a> `00bb9e94` | `08 09 00 37` | tbnz w8,#0x0,0x00bb9fb4 | `CONDITIONAL_JUMP`
<a id="insn-00bb9e98"></a> `00bb9e98` | `68 a2 41 39` | ldrb w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bb9e9c"></a> `00bb9e9c` | `48 09 00 37` | tbnz w8,#0x0,0x00bb9fc4 | `CONDITIONAL_JUMP`
<a id="insn-00bb9ea0"></a> `00bb9ea0` | `68 42 41 39` | ldrb w8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00bb9ea4"></a> `00bb9ea4` | `88 09 00 37` | tbnz w8,#0x0,0x00bb9fd4 | `CONDITIONAL_JUMP`
<a id="insn-00bb9ea8"></a> `00bb9ea8` | `68 e2 40 39` | ldrb w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bb9eac"></a> `00bb9eac` | `c8 09 00 37` | tbnz w8,#0x0,0x00bb9fe4 | `CONDITIONAL_JUMP`
<a id="insn-00bb9eb0"></a> `00bb9eb0` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bb9eb4"></a> `00bb9eb4` | `08 0a 00 37` | tbnz w8,#0x0,0x00bb9ff4 | `CONDITIONAL_JUMP`
<a id="insn-00bb9eb8"></a> `00bb9eb8` | `68 22 40 39` | ldrb w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb9ebc"></a> `00bb9ebc` | `68 00 00 36` | tbz w8,#0x0,0x00bb9ec8 | `CONDITIONAL_JUMP`
<a id="insn-00bb9ec0"></a> `00bb9ec0` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bb9ec4"></a> `00bb9ec4` | `67 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9ec8"></a> `00bb9ec8` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bb9ecc"></a> `00bb9ecc` | `99 9e 00 94` | bl 0x00be1930 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9ed0"></a> `00bb9ed0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb9ed4"></a> `00bb9ed4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb9ed8"></a> `00bb9ed8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb9edc"></a> `00bb9edc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb9ee0"></a> `00bb9ee0` | `60 12 42 f9` | ldr x0,[x19, #0x420] | `FALL_THROUGH`
<a id="insn-00bb9ee4"></a> `00bb9ee4` | `5f 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9ee8"></a> `00bb9ee8` | `68 e2 4f 39` | ldrb w8,[x19, #0x3f8] | `FALL_THROUGH`
<a id="insn-00bb9eec"></a> `00bb9eec` | `a8 f8 07 36` | tbz w8,#0x0,0x00bb9e00 | `CONDITIONAL_JUMP`
<a id="insn-00bb9ef0"></a> `00bb9ef0` | `60 06 42 f9` | ldr x0,[x19, #0x408] | `FALL_THROUGH`
<a id="insn-00bb9ef4"></a> `00bb9ef4` | `5b 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9ef8"></a> `00bb9ef8` | `68 82 4f 39` | ldrb w8,[x19, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bb9efc"></a> `00bb9efc` | `68 f8 07 36` | tbz w8,#0x0,0x00bb9e08 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f00"></a> `00bb9f00` | `60 fa 41 f9` | ldr x0,[x19, #0x3f0] | `FALL_THROUGH`
<a id="insn-00bb9f04"></a> `00bb9f04` | `57 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f08"></a> `00bb9f08` | `68 22 4f 39` | ldrb w8,[x19, #0x3c8] | `FALL_THROUGH`
<a id="insn-00bb9f0c"></a> `00bb9f0c` | `28 f8 07 36` | tbz w8,#0x0,0x00bb9e10 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f10"></a> `00bb9f10` | `60 ee 41 f9` | ldr x0,[x19, #0x3d8] | `FALL_THROUGH`
<a id="insn-00bb9f14"></a> `00bb9f14` | `53 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f18"></a> `00bb9f18` | `68 c2 4e 39` | ldrb w8,[x19, #0x3b0] | `FALL_THROUGH`
<a id="insn-00bb9f1c"></a> `00bb9f1c` | `e8 f7 07 36` | tbz w8,#0x0,0x00bb9e18 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f20"></a> `00bb9f20` | `60 e2 41 f9` | ldr x0,[x19, #0x3c0] | `FALL_THROUGH`
<a id="insn-00bb9f24"></a> `00bb9f24` | `4f 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f28"></a> `00bb9f28` | `68 62 4e 39` | ldrb w8,[x19, #0x398] | `FALL_THROUGH`
<a id="insn-00bb9f2c"></a> `00bb9f2c` | `a8 f7 07 37` | tbnz w8,#0x0,0x00bb9e20 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f30"></a> `00bb9f30` | `be ff ff 17` | b 0x00bb9e28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb9f34"></a> `00bb9f34` | `60 aa 40 f9` | ldr x0,[x19, #0x150] | `FALL_THROUGH`
<a id="insn-00bb9f38"></a> `00bb9f38` | `4a 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f3c"></a> `00bb9f3c` | `68 a2 44 39` | ldrb w8,[x19, #0x128] | `FALL_THROUGH`
<a id="insn-00bb9f40"></a> `00bb9f40` | `08 f9 07 36` | tbz w8,#0x0,0x00bb9e60 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f44"></a> `00bb9f44` | `60 9e 40 f9` | ldr x0,[x19, #0x138] | `FALL_THROUGH`
<a id="insn-00bb9f48"></a> `00bb9f48` | `46 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f4c"></a> `00bb9f4c` | `68 42 44 39` | ldrb w8,[x19, #0x110] | `FALL_THROUGH`
<a id="insn-00bb9f50"></a> `00bb9f50` | `c8 f8 07 36` | tbz w8,#0x0,0x00bb9e68 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f54"></a> `00bb9f54` | `60 92 40 f9` | ldr x0,[x19, #0x120] | `FALL_THROUGH`
<a id="insn-00bb9f58"></a> `00bb9f58` | `42 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f5c"></a> `00bb9f5c` | `68 e2 43 39` | ldrb w8,[x19, #0xf8] | `FALL_THROUGH`
<a id="insn-00bb9f60"></a> `00bb9f60` | `88 f8 07 36` | tbz w8,#0x0,0x00bb9e70 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f64"></a> `00bb9f64` | `60 86 40 f9` | ldr x0,[x19, #0x108] | `FALL_THROUGH`
<a id="insn-00bb9f68"></a> `00bb9f68` | `3e 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f6c"></a> `00bb9f6c` | `68 82 43 39` | ldrb w8,[x19, #0xe0] | `FALL_THROUGH`
<a id="insn-00bb9f70"></a> `00bb9f70` | `48 f8 07 36` | tbz w8,#0x0,0x00bb9e78 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f74"></a> `00bb9f74` | `60 7a 40 f9` | ldr x0,[x19, #0xf0] | `FALL_THROUGH`
<a id="insn-00bb9f78"></a> `00bb9f78` | `3a 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f7c"></a> `00bb9f7c` | `68 22 43 39` | ldrb w8,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-00bb9f80"></a> `00bb9f80` | `08 f8 07 36` | tbz w8,#0x0,0x00bb9e80 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f84"></a> `00bb9f84` | `60 6e 40 f9` | ldr x0,[x19, #0xd8] | `FALL_THROUGH`
<a id="insn-00bb9f88"></a> `00bb9f88` | `36 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f8c"></a> `00bb9f8c` | `68 c2 42 39` | ldrb w8,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-00bb9f90"></a> `00bb9f90` | `c8 f7 07 36` | tbz w8,#0x0,0x00bb9e88 | `CONDITIONAL_JUMP`
<a id="insn-00bb9f94"></a> `00bb9f94` | `60 62 40 f9` | ldr x0,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00bb9f98"></a> `00bb9f98` | `32 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9f9c"></a> `00bb9f9c` | `68 62 42 39` | ldrb w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bb9fa0"></a> `00bb9fa0` | `88 f7 07 36` | tbz w8,#0x0,0x00bb9e90 | `CONDITIONAL_JUMP`
<a id="insn-00bb9fa4"></a> `00bb9fa4` | `60 56 40 f9` | ldr x0,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-00bb9fa8"></a> `00bb9fa8` | `2e 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9fac"></a> `00bb9fac` | `68 02 42 39` | ldrb w8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bb9fb0"></a> `00bb9fb0` | `48 f7 07 36` | tbz w8,#0x0,0x00bb9e98 | `CONDITIONAL_JUMP`
<a id="insn-00bb9fb4"></a> `00bb9fb4` | `60 4a 40 f9` | ldr x0,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bb9fb8"></a> `00bb9fb8` | `2a 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9fbc"></a> `00bb9fbc` | `68 a2 41 39` | ldrb w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bb9fc0"></a> `00bb9fc0` | `08 f7 07 36` | tbz w8,#0x0,0x00bb9ea0 | `CONDITIONAL_JUMP`
<a id="insn-00bb9fc4"></a> `00bb9fc4` | `60 3e 40 f9` | ldr x0,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bb9fc8"></a> `00bb9fc8` | `26 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9fcc"></a> `00bb9fcc` | `68 42 41 39` | ldrb w8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00bb9fd0"></a> `00bb9fd0` | `c8 f6 07 36` | tbz w8,#0x0,0x00bb9ea8 | `CONDITIONAL_JUMP`
<a id="insn-00bb9fd4"></a> `00bb9fd4` | `60 32 40 f9` | ldr x0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bb9fd8"></a> `00bb9fd8` | `22 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9fdc"></a> `00bb9fdc` | `68 e2 40 39` | ldrb w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bb9fe0"></a> `00bb9fe0` | `88 f6 07 36` | tbz w8,#0x0,0x00bb9eb0 | `CONDITIONAL_JUMP`
<a id="insn-00bb9fe4"></a> `00bb9fe4` | `60 26 40 f9` | ldr x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb9fe8"></a> `00bb9fe8` | `1e 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9fec"></a> `00bb9fec` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bb9ff0"></a> `00bb9ff0` | `48 f6 07 36` | tbz w8,#0x0,0x00bb9eb8 | `CONDITIONAL_JUMP`
<a id="insn-00bb9ff4"></a> `00bb9ff4` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bb9ff8"></a> `00bb9ff8` | `1a 84 00 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9ffc"></a> `00bb9ffc` | `68 22 40 39` | ldrb w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bba000"></a> `00bba000` | `08 f6 07 37` | tbnz w8,#0x0,0x00bb9ec0 | `CONDITIONAL_JUMP`
<a id="insn-00bba004"></a> `00bba004` | `b1 ff ff 17` | b 0x00bb9ec8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bb9ddc`](#insn-00bb9ddc) 範囲 `[['00bb9ddc', '00bb9df7']]`
  - `CONDITIONAL_JUMP` [`00bb9df4`](#insn-00bb9df4) → [`00bb9ee0`](#insn-00bb9ee0)
  - `FALL_THROUGH` [`00bb9df4`](#insn-00bb9df4) → [`00bb9df8`](#insn-00bb9df8)
- ブロック [`00bb9df8`](#insn-00bb9df8) 範囲 `[['00bb9df8', '00bb9dff']]`
  - `CONDITIONAL_JUMP` [`00bb9dfc`](#insn-00bb9dfc) → [`00bb9ef0`](#insn-00bb9ef0)
  - `FALL_THROUGH` [`00bb9dfc`](#insn-00bb9dfc) → [`00bb9e00`](#insn-00bb9e00)
- ブロック [`00bb9e00`](#insn-00bb9e00) 範囲 `[['00bb9e00', '00bb9e07']]`
  - `CONDITIONAL_JUMP` [`00bb9e04`](#insn-00bb9e04) → [`00bb9f00`](#insn-00bb9f00)
  - `FALL_THROUGH` [`00bb9e04`](#insn-00bb9e04) → [`00bb9e08`](#insn-00bb9e08)
- ブロック [`00bb9e08`](#insn-00bb9e08) 範囲 `[['00bb9e08', '00bb9e0f']]`
  - `CONDITIONAL_JUMP` [`00bb9e0c`](#insn-00bb9e0c) → [`00bb9f10`](#insn-00bb9f10)
  - `FALL_THROUGH` [`00bb9e0c`](#insn-00bb9e0c) → [`00bb9e10`](#insn-00bb9e10)
- ブロック [`00bb9e10`](#insn-00bb9e10) 範囲 `[['00bb9e10', '00bb9e17']]`
  - `CONDITIONAL_JUMP` [`00bb9e14`](#insn-00bb9e14) → [`00bb9f20`](#insn-00bb9f20)
  - `FALL_THROUGH` [`00bb9e14`](#insn-00bb9e14) → [`00bb9e18`](#insn-00bb9e18)
- ブロック [`00bb9e18`](#insn-00bb9e18) 範囲 `[['00bb9e18', '00bb9e1f']]`
  - `CONDITIONAL_JUMP` [`00bb9e1c`](#insn-00bb9e1c) → [`00bb9e28`](#insn-00bb9e28)
  - `FALL_THROUGH` [`00bb9e1c`](#insn-00bb9e1c) → [`00bb9e20`](#insn-00bb9e20)
- ブロック [`00bb9e20`](#insn-00bb9e20) 範囲 `[['00bb9e20', '00bb9e23']]`
  - `FALL_THROUGH` [`00bb9e20`](#insn-00bb9e20) → [`00bb9e24`](#insn-00bb9e24)
- ブロック [`00bb9e24`](#insn-00bb9e24) 範囲 `[['00bb9e24', '00bb9e27']]`
  - `FALL_THROUGH` [`00bb9e24`](#insn-00bb9e24) → [`00bb9e28`](#insn-00bb9e28)
- ブロック [`00bb9e28`](#insn-00bb9e28) 範囲 `[['00bb9e28', '00bb9e2f']]`
  - `UNCONDITIONAL_JUMP` [`00bb9e2c`](#insn-00bb9e2c) → [`00bb9e38`](#insn-00bb9e38)
- ブロック [`00bb9e30`](#insn-00bb9e30) 範囲 `[['00bb9e30', '00bb9e37']]`
  - `CONDITIONAL_JUMP` [`00bb9e34`](#insn-00bb9e34) → [`00bb9e50`](#insn-00bb9e50)
  - `FALL_THROUGH` [`00bb9e34`](#insn-00bb9e34) → [`00bb9e38`](#insn-00bb9e38)
- ブロック [`00bb9e38`](#insn-00bb9e38) 範囲 `[['00bb9e38', '00bb9e43']]`
  - `CONDITIONAL_JUMP` [`00bb9e40`](#insn-00bb9e40) → [`00bb9e30`](#insn-00bb9e30)
  - `FALL_THROUGH` [`00bb9e40`](#insn-00bb9e40) → [`00bb9e44`](#insn-00bb9e44)
- ブロック [`00bb9e44`](#insn-00bb9e44) 範囲 `[['00bb9e44', '00bb9e4f']]`
  - `UNCONDITIONAL_JUMP` [`00bb9e4c`](#insn-00bb9e4c) → [`00bb9e30`](#insn-00bb9e30)
- ブロック [`00bb9e50`](#insn-00bb9e50) 範囲 `[['00bb9e50', '00bb9e57']]`
  - `CONDITIONAL_JUMP` [`00bb9e54`](#insn-00bb9e54) → [`00bb9f34`](#insn-00bb9f34)
  - `FALL_THROUGH` [`00bb9e54`](#insn-00bb9e54) → [`00bb9e58`](#insn-00bb9e58)
- ブロック [`00bb9e58`](#insn-00bb9e58) 範囲 `[['00bb9e58', '00bb9e5f']]`
  - `CONDITIONAL_JUMP` [`00bb9e5c`](#insn-00bb9e5c) → [`00bb9f44`](#insn-00bb9f44)
  - `FALL_THROUGH` [`00bb9e5c`](#insn-00bb9e5c) → [`00bb9e60`](#insn-00bb9e60)
- ブロック [`00bb9e60`](#insn-00bb9e60) 範囲 `[['00bb9e60', '00bb9e67']]`
  - `CONDITIONAL_JUMP` [`00bb9e64`](#insn-00bb9e64) → [`00bb9f54`](#insn-00bb9f54)
  - `FALL_THROUGH` [`00bb9e64`](#insn-00bb9e64) → [`00bb9e68`](#insn-00bb9e68)
- ブロック [`00bb9e68`](#insn-00bb9e68) 範囲 `[['00bb9e68', '00bb9e6f']]`
  - `CONDITIONAL_JUMP` [`00bb9e6c`](#insn-00bb9e6c) → [`00bb9f64`](#insn-00bb9f64)
  - `FALL_THROUGH` [`00bb9e6c`](#insn-00bb9e6c) → [`00bb9e70`](#insn-00bb9e70)
- ブロック [`00bb9e70`](#insn-00bb9e70) 範囲 `[['00bb9e70', '00bb9e77']]`
  - `CONDITIONAL_JUMP` [`00bb9e74`](#insn-00bb9e74) → [`00bb9f74`](#insn-00bb9f74)
  - `FALL_THROUGH` [`00bb9e74`](#insn-00bb9e74) → [`00bb9e78`](#insn-00bb9e78)
- ブロック [`00bb9e78`](#insn-00bb9e78) 範囲 `[['00bb9e78', '00bb9e7f']]`
  - `CONDITIONAL_JUMP` [`00bb9e7c`](#insn-00bb9e7c) → [`00bb9f84`](#insn-00bb9f84)
  - `FALL_THROUGH` [`00bb9e7c`](#insn-00bb9e7c) → [`00bb9e80`](#insn-00bb9e80)
- ブロック [`00bb9e80`](#insn-00bb9e80) 範囲 `[['00bb9e80', '00bb9e87']]`
  - `CONDITIONAL_JUMP` [`00bb9e84`](#insn-00bb9e84) → [`00bb9f94`](#insn-00bb9f94)
  - `FALL_THROUGH` [`00bb9e84`](#insn-00bb9e84) → [`00bb9e88`](#insn-00bb9e88)
- ブロック [`00bb9e88`](#insn-00bb9e88) 範囲 `[['00bb9e88', '00bb9e8f']]`
  - `CONDITIONAL_JUMP` [`00bb9e8c`](#insn-00bb9e8c) → [`00bb9fa4`](#insn-00bb9fa4)
  - `FALL_THROUGH` [`00bb9e8c`](#insn-00bb9e8c) → [`00bb9e90`](#insn-00bb9e90)
- ブロック [`00bb9e90`](#insn-00bb9e90) 範囲 `[['00bb9e90', '00bb9e97']]`
  - `CONDITIONAL_JUMP` [`00bb9e94`](#insn-00bb9e94) → [`00bb9fb4`](#insn-00bb9fb4)
  - `FALL_THROUGH` [`00bb9e94`](#insn-00bb9e94) → [`00bb9e98`](#insn-00bb9e98)
- ブロック [`00bb9e98`](#insn-00bb9e98) 範囲 `[['00bb9e98', '00bb9e9f']]`
  - `CONDITIONAL_JUMP` [`00bb9e9c`](#insn-00bb9e9c) → [`00bb9fc4`](#insn-00bb9fc4)
  - `FALL_THROUGH` [`00bb9e9c`](#insn-00bb9e9c) → [`00bb9ea0`](#insn-00bb9ea0)
- ブロック [`00bb9ea0`](#insn-00bb9ea0) 範囲 `[['00bb9ea0', '00bb9ea7']]`
  - `CONDITIONAL_JUMP` [`00bb9ea4`](#insn-00bb9ea4) → [`00bb9fd4`](#insn-00bb9fd4)
  - `FALL_THROUGH` [`00bb9ea4`](#insn-00bb9ea4) → [`00bb9ea8`](#insn-00bb9ea8)
- ブロック [`00bb9ea8`](#insn-00bb9ea8) 範囲 `[['00bb9ea8', '00bb9eaf']]`
  - `CONDITIONAL_JUMP` [`00bb9eac`](#insn-00bb9eac) → [`00bb9fe4`](#insn-00bb9fe4)
  - `FALL_THROUGH` [`00bb9eac`](#insn-00bb9eac) → [`00bb9eb0`](#insn-00bb9eb0)
- ブロック [`00bb9eb0`](#insn-00bb9eb0) 範囲 `[['00bb9eb0', '00bb9eb7']]`
  - `CONDITIONAL_JUMP` [`00bb9eb4`](#insn-00bb9eb4) → [`00bb9ff4`](#insn-00bb9ff4)
  - `FALL_THROUGH` [`00bb9eb4`](#insn-00bb9eb4) → [`00bb9eb8`](#insn-00bb9eb8)
- ブロック [`00bb9eb8`](#insn-00bb9eb8) 範囲 `[['00bb9eb8', '00bb9ebf']]`
  - `CONDITIONAL_JUMP` [`00bb9ebc`](#insn-00bb9ebc) → [`00bb9ec8`](#insn-00bb9ec8)
  - `FALL_THROUGH` [`00bb9ebc`](#insn-00bb9ebc) → [`00bb9ec0`](#insn-00bb9ec0)
- ブロック [`00bb9ec0`](#insn-00bb9ec0) 範囲 `[['00bb9ec0', '00bb9ec7']]`
  - `FALL_THROUGH` [`00bb9ec4`](#insn-00bb9ec4) → [`00bb9ec8`](#insn-00bb9ec8)
- ブロック [`00bb9ec8`](#insn-00bb9ec8) 範囲 `[['00bb9ec8', '00bb9edf']]`
- ブロック [`00bb9ee0`](#insn-00bb9ee0) 範囲 `[['00bb9ee0', '00bb9eef']]`
  - `CONDITIONAL_JUMP` [`00bb9eec`](#insn-00bb9eec) → [`00bb9e00`](#insn-00bb9e00)
  - `FALL_THROUGH` [`00bb9eec`](#insn-00bb9eec) → [`00bb9ef0`](#insn-00bb9ef0)
- ブロック [`00bb9ef0`](#insn-00bb9ef0) 範囲 `[['00bb9ef0', '00bb9eff']]`
  - `CONDITIONAL_JUMP` [`00bb9efc`](#insn-00bb9efc) → [`00bb9e08`](#insn-00bb9e08)
  - `FALL_THROUGH` [`00bb9efc`](#insn-00bb9efc) → [`00bb9f00`](#insn-00bb9f00)
- ブロック [`00bb9f00`](#insn-00bb9f00) 範囲 `[['00bb9f00', '00bb9f03']]`
  - `FALL_THROUGH` [`00bb9f00`](#insn-00bb9f00) → [`00bb9f04`](#insn-00bb9f04)
- ブロック [`00bb9f04`](#insn-00bb9f04) 範囲 `[['00bb9f04', '00bb9f0f']]`
  - `CONDITIONAL_JUMP` [`00bb9f0c`](#insn-00bb9f0c) → [`00bb9e10`](#insn-00bb9e10)
  - `FALL_THROUGH` [`00bb9f0c`](#insn-00bb9f0c) → [`00bb9f10`](#insn-00bb9f10)
- ブロック [`00bb9f10`](#insn-00bb9f10) 範囲 `[['00bb9f10', '00bb9f1f']]`
  - `CONDITIONAL_JUMP` [`00bb9f1c`](#insn-00bb9f1c) → [`00bb9e18`](#insn-00bb9e18)
  - `FALL_THROUGH` [`00bb9f1c`](#insn-00bb9f1c) → [`00bb9f20`](#insn-00bb9f20)
- ブロック [`00bb9f20`](#insn-00bb9f20) 範囲 `[['00bb9f20', '00bb9f2f']]`
  - `CONDITIONAL_JUMP` [`00bb9f2c`](#insn-00bb9f2c) → [`00bb9e20`](#insn-00bb9e20)
  - `FALL_THROUGH` [`00bb9f2c`](#insn-00bb9f2c) → [`00bb9f30`](#insn-00bb9f30)
- ブロック [`00bb9f30`](#insn-00bb9f30) 範囲 `[['00bb9f30', '00bb9f33']]`
  - `UNCONDITIONAL_JUMP` [`00bb9f30`](#insn-00bb9f30) → [`00bb9e28`](#insn-00bb9e28)
- ブロック [`00bb9f34`](#insn-00bb9f34) 範囲 `[['00bb9f34', '00bb9f43']]`
  - `CONDITIONAL_JUMP` [`00bb9f40`](#insn-00bb9f40) → [`00bb9e60`](#insn-00bb9e60)
  - `FALL_THROUGH` [`00bb9f40`](#insn-00bb9f40) → [`00bb9f44`](#insn-00bb9f44)
- ブロック [`00bb9f44`](#insn-00bb9f44) 範囲 `[['00bb9f44', '00bb9f53']]`
  - `CONDITIONAL_JUMP` [`00bb9f50`](#insn-00bb9f50) → [`00bb9e68`](#insn-00bb9e68)
  - `FALL_THROUGH` [`00bb9f50`](#insn-00bb9f50) → [`00bb9f54`](#insn-00bb9f54)
- ブロック [`00bb9f54`](#insn-00bb9f54) 範囲 `[['00bb9f54', '00bb9f63']]`
  - `CONDITIONAL_JUMP` [`00bb9f60`](#insn-00bb9f60) → [`00bb9e70`](#insn-00bb9e70)
  - `FALL_THROUGH` [`00bb9f60`](#insn-00bb9f60) → [`00bb9f64`](#insn-00bb9f64)
- ブロック [`00bb9f64`](#insn-00bb9f64) 範囲 `[['00bb9f64', '00bb9f73']]`
  - `CONDITIONAL_JUMP` [`00bb9f70`](#insn-00bb9f70) → [`00bb9e78`](#insn-00bb9e78)
  - `FALL_THROUGH` [`00bb9f70`](#insn-00bb9f70) → [`00bb9f74`](#insn-00bb9f74)
- ブロック [`00bb9f74`](#insn-00bb9f74) 範囲 `[['00bb9f74', '00bb9f83']]`
  - `CONDITIONAL_JUMP` [`00bb9f80`](#insn-00bb9f80) → [`00bb9e80`](#insn-00bb9e80)
  - `FALL_THROUGH` [`00bb9f80`](#insn-00bb9f80) → [`00bb9f84`](#insn-00bb9f84)
- ブロック [`00bb9f84`](#insn-00bb9f84) 範囲 `[['00bb9f84', '00bb9f93']]`
  - `CONDITIONAL_JUMP` [`00bb9f90`](#insn-00bb9f90) → [`00bb9e88`](#insn-00bb9e88)
  - `FALL_THROUGH` [`00bb9f90`](#insn-00bb9f90) → [`00bb9f94`](#insn-00bb9f94)
- ブロック [`00bb9f94`](#insn-00bb9f94) 範囲 `[['00bb9f94', '00bb9fa3']]`
  - `CONDITIONAL_JUMP` [`00bb9fa0`](#insn-00bb9fa0) → [`00bb9e90`](#insn-00bb9e90)
  - `FALL_THROUGH` [`00bb9fa0`](#insn-00bb9fa0) → [`00bb9fa4`](#insn-00bb9fa4)
- ブロック [`00bb9fa4`](#insn-00bb9fa4) 範囲 `[['00bb9fa4', '00bb9fb3']]`
  - `CONDITIONAL_JUMP` [`00bb9fb0`](#insn-00bb9fb0) → [`00bb9e98`](#insn-00bb9e98)
  - `FALL_THROUGH` [`00bb9fb0`](#insn-00bb9fb0) → [`00bb9fb4`](#insn-00bb9fb4)
- ブロック [`00bb9fb4`](#insn-00bb9fb4) 範囲 `[['00bb9fb4', '00bb9fc3']]`
  - `CONDITIONAL_JUMP` [`00bb9fc0`](#insn-00bb9fc0) → [`00bb9ea0`](#insn-00bb9ea0)
  - `FALL_THROUGH` [`00bb9fc0`](#insn-00bb9fc0) → [`00bb9fc4`](#insn-00bb9fc4)
- ブロック [`00bb9fc4`](#insn-00bb9fc4) 範囲 `[['00bb9fc4', '00bb9fd3']]`
  - `CONDITIONAL_JUMP` [`00bb9fd0`](#insn-00bb9fd0) → [`00bb9ea8`](#insn-00bb9ea8)
  - `FALL_THROUGH` [`00bb9fd0`](#insn-00bb9fd0) → [`00bb9fd4`](#insn-00bb9fd4)
- ブロック [`00bb9fd4`](#insn-00bb9fd4) 範囲 `[['00bb9fd4', '00bb9fe3']]`
  - `CONDITIONAL_JUMP` [`00bb9fe0`](#insn-00bb9fe0) → [`00bb9eb0`](#insn-00bb9eb0)
  - `FALL_THROUGH` [`00bb9fe0`](#insn-00bb9fe0) → [`00bb9fe4`](#insn-00bb9fe4)
- ブロック [`00bb9fe4`](#insn-00bb9fe4) 範囲 `[['00bb9fe4', '00bb9ff3']]`
  - `CONDITIONAL_JUMP` [`00bb9ff0`](#insn-00bb9ff0) → [`00bb9eb8`](#insn-00bb9eb8)
  - `FALL_THROUGH` [`00bb9ff0`](#insn-00bb9ff0) → [`00bb9ff4`](#insn-00bb9ff4)
- ブロック [`00bb9ff4`](#insn-00bb9ff4) 範囲 `[['00bb9ff4', '00bba003']]`
  - `CONDITIONAL_JUMP` [`00bba000`](#insn-00bba000) → [`00bb9ec0`](#insn-00bb9ec0)
  - `FALL_THROUGH` [`00bba000`](#insn-00bba000) → [`00bba004`](#insn-00bba004)
- ブロック [`00bba004`](#insn-00bba004) 範囲 `[['00bba004', '00bba007']]`
  - `UNCONDITIONAL_JUMP` [`00bba004`](#insn-00bba004) → [`00bb9ec8`](#insn-00bb9ec8)

## 命令位置別の参照

- [`00bb9de0`](#insn-00bb9de0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9de4`](#insn-00bb9de4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9df4`](#insn-00bb9df4) → [`00bb9ee0`](#insn-00bb9ee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9dfc`](#insn-00bb9dfc) → [`00bb9ef0`](#insn-00bb9ef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e04`](#insn-00bb9e04) → [`00bb9f00`](#insn-00bb9f00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e0c`](#insn-00bb9e0c) → [`00bb9f10`](#insn-00bb9f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e14`](#insn-00bb9e14) → [`00bb9f20`](#insn-00bb9f20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e1c`](#insn-00bb9e1c) → [`00bb9e28`](#insn-00bb9e28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e24`](#insn-00bb9e24) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e2c`](#insn-00bb9e2c) → [`00bb9e38`](#insn-00bb9e38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e34`](#insn-00bb9e34) → [`00bb9e50`](#insn-00bb9e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e40`](#insn-00bb9e40) → [`00bb9e30`](#insn-00bb9e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e48`](#insn-00bb9e48) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e4c`](#insn-00bb9e4c) → [`00bb9e30`](#insn-00bb9e30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e54`](#insn-00bb9e54) → [`00bb9f34`](#insn-00bb9f34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e5c`](#insn-00bb9e5c) → [`00bb9f44`](#insn-00bb9f44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e64`](#insn-00bb9e64) → [`00bb9f54`](#insn-00bb9f54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e6c`](#insn-00bb9e6c) → [`00bb9f64`](#insn-00bb9f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e74`](#insn-00bb9e74) → [`00bb9f74`](#insn-00bb9f74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e7c`](#insn-00bb9e7c) → [`00bb9f84`](#insn-00bb9f84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e84`](#insn-00bb9e84) → [`00bb9f94`](#insn-00bb9f94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e8c`](#insn-00bb9e8c) → [`00bb9fa4`](#insn-00bb9fa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e94`](#insn-00bb9e94) → [`00bb9fb4`](#insn-00bb9fb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9e9c`](#insn-00bb9e9c) → [`00bb9fc4`](#insn-00bb9fc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ea4`](#insn-00bb9ea4) → [`00bb9fd4`](#insn-00bb9fd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9eac`](#insn-00bb9eac) → [`00bb9fe4`](#insn-00bb9fe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9eb4`](#insn-00bb9eb4) → [`00bb9ff4`](#insn-00bb9ff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ebc`](#insn-00bb9ebc) → [`00bb9ec8`](#insn-00bb9ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ec4`](#insn-00bb9ec4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ecc`](#insn-00bb9ecc) → [`00be1930`](../00be1/00be1930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1930` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ed0`](#insn-00bb9ed0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ed4`](#insn-00bb9ed4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ee4`](#insn-00bb9ee4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9eec`](#insn-00bb9eec) → [`00bb9e00`](#insn-00bb9e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ef4`](#insn-00bb9ef4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9efc`](#insn-00bb9efc) → [`00bb9e08`](#insn-00bb9e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f04`](#insn-00bb9f04) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f0c`](#insn-00bb9f0c) → [`00bb9e10`](#insn-00bb9e10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f14`](#insn-00bb9f14) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f1c`](#insn-00bb9f1c) → [`00bb9e18`](#insn-00bb9e18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f24`](#insn-00bb9f24) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f2c`](#insn-00bb9f2c) → [`00bb9e20`](#insn-00bb9e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f30`](#insn-00bb9f30) → [`00bb9e28`](#insn-00bb9e28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f38`](#insn-00bb9f38) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f40`](#insn-00bb9f40) → [`00bb9e60`](#insn-00bb9e60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f48`](#insn-00bb9f48) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f50`](#insn-00bb9f50) → [`00bb9e68`](#insn-00bb9e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f58`](#insn-00bb9f58) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f60`](#insn-00bb9f60) → [`00bb9e70`](#insn-00bb9e70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f68`](#insn-00bb9f68) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f70`](#insn-00bb9f70) → [`00bb9e78`](#insn-00bb9e78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f78`](#insn-00bb9f78) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f80`](#insn-00bb9f80) → [`00bb9e80`](#insn-00bb9e80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f88`](#insn-00bb9f88) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f90`](#insn-00bb9f90) → [`00bb9e88`](#insn-00bb9e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9f98`](#insn-00bb9f98) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fa0`](#insn-00bb9fa0) → [`00bb9e90`](#insn-00bb9e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fa8`](#insn-00bb9fa8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fb0`](#insn-00bb9fb0) → [`00bb9e98`](#insn-00bb9e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fb8`](#insn-00bb9fb8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fc0`](#insn-00bb9fc0) → [`00bb9ea0`](#insn-00bb9ea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fc8`](#insn-00bb9fc8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fd0`](#insn-00bb9fd0) → [`00bb9ea8`](#insn-00bb9ea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fd8`](#insn-00bb9fd8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fe0`](#insn-00bb9fe0) → [`00bb9eb0`](#insn-00bb9eb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9fe8`](#insn-00bb9fe8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ff0`](#insn-00bb9ff0) → [`00bb9eb8`](#insn-00bb9eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9ff8`](#insn-00bb9ff8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00bba000`](#insn-00bba000) → [`00bb9ec0`](#insn-00bb9ec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba004`](#insn-00bba004) → [`00bb9ec8`](#insn-00bb9ec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb9de0`](#insn-00bb9de0)

~~~json
{
  "source": "00bb9de0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9de4`](#insn-00bb9de4)

~~~json
{
  "source": "00bb9de4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9df4`](#insn-00bb9df4)

~~~json
{
  "source": "00bb9df4",
  "target": "00bb9ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9dfc`](#insn-00bb9dfc)

~~~json
{
  "source": "00bb9dfc",
  "target": "00bb9ef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e04`](#insn-00bb9e04)

~~~json
{
  "source": "00bb9e04",
  "target": "00bb9f00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e0c`](#insn-00bb9e0c)

~~~json
{
  "source": "00bb9e0c",
  "target": "00bb9f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e14`](#insn-00bb9e14)

~~~json
{
  "source": "00bb9e14",
  "target": "00bb9f20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e1c`](#insn-00bb9e1c)

~~~json
{
  "source": "00bb9e1c",
  "target": "00bb9e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e24`](#insn-00bb9e24)

~~~json
{
  "source": "00bb9e24",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9e2c`](#insn-00bb9e2c)

~~~json
{
  "source": "00bb9e2c",
  "target": "00bb9e38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e34`](#insn-00bb9e34)

~~~json
{
  "source": "00bb9e34",
  "target": "00bb9e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e40`](#insn-00bb9e40)

~~~json
{
  "source": "00bb9e40",
  "target": "00bb9e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e48`](#insn-00bb9e48)

~~~json
{
  "source": "00bb9e48",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9e4c`](#insn-00bb9e4c)

~~~json
{
  "source": "00bb9e4c",
  "target": "00bb9e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e54`](#insn-00bb9e54)

~~~json
{
  "source": "00bb9e54",
  "target": "00bb9f34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e5c`](#insn-00bb9e5c)

~~~json
{
  "source": "00bb9e5c",
  "target": "00bb9f44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e64`](#insn-00bb9e64)

~~~json
{
  "source": "00bb9e64",
  "target": "00bb9f54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e6c`](#insn-00bb9e6c)

~~~json
{
  "source": "00bb9e6c",
  "target": "00bb9f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e74`](#insn-00bb9e74)

~~~json
{
  "source": "00bb9e74",
  "target": "00bb9f74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e7c`](#insn-00bb9e7c)

~~~json
{
  "source": "00bb9e7c",
  "target": "00bb9f84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e84`](#insn-00bb9e84)

~~~json
{
  "source": "00bb9e84",
  "target": "00bb9f94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e8c`](#insn-00bb9e8c)

~~~json
{
  "source": "00bb9e8c",
  "target": "00bb9fa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e94`](#insn-00bb9e94)

~~~json
{
  "source": "00bb9e94",
  "target": "00bb9fb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9e9c`](#insn-00bb9e9c)

~~~json
{
  "source": "00bb9e9c",
  "target": "00bb9fc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ea4`](#insn-00bb9ea4)

~~~json
{
  "source": "00bb9ea4",
  "target": "00bb9fd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9eac`](#insn-00bb9eac)

~~~json
{
  "source": "00bb9eac",
  "target": "00bb9fe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9eb4`](#insn-00bb9eb4)

~~~json
{
  "source": "00bb9eb4",
  "target": "00bb9ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ebc`](#insn-00bb9ebc)

~~~json
{
  "source": "00bb9ebc",
  "target": "00bb9ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ec4`](#insn-00bb9ec4)

~~~json
{
  "source": "00bb9ec4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9ecc`](#insn-00bb9ecc)

~~~json
{
  "source": "00bb9ecc",
  "target": "00be1930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9ed0`](#insn-00bb9ed0)

~~~json
{
  "source": "00bb9ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ed4`](#insn-00bb9ed4)

~~~json
{
  "source": "00bb9ed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ee4`](#insn-00bb9ee4)

~~~json
{
  "source": "00bb9ee4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9eec`](#insn-00bb9eec)

~~~json
{
  "source": "00bb9eec",
  "target": "00bb9e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ef4`](#insn-00bb9ef4)

~~~json
{
  "source": "00bb9ef4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9efc`](#insn-00bb9efc)

~~~json
{
  "source": "00bb9efc",
  "target": "00bb9e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f04`](#insn-00bb9f04)

~~~json
{
  "source": "00bb9f04",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f0c`](#insn-00bb9f0c)

~~~json
{
  "source": "00bb9f0c",
  "target": "00bb9e10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f14`](#insn-00bb9f14)

~~~json
{
  "source": "00bb9f14",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f1c`](#insn-00bb9f1c)

~~~json
{
  "source": "00bb9f1c",
  "target": "00bb9e18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f24`](#insn-00bb9f24)

~~~json
{
  "source": "00bb9f24",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f2c`](#insn-00bb9f2c)

~~~json
{
  "source": "00bb9f2c",
  "target": "00bb9e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f30`](#insn-00bb9f30)

~~~json
{
  "source": "00bb9f30",
  "target": "00bb9e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f38`](#insn-00bb9f38)

~~~json
{
  "source": "00bb9f38",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f40`](#insn-00bb9f40)

~~~json
{
  "source": "00bb9f40",
  "target": "00bb9e60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f48`](#insn-00bb9f48)

~~~json
{
  "source": "00bb9f48",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f50`](#insn-00bb9f50)

~~~json
{
  "source": "00bb9f50",
  "target": "00bb9e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f58`](#insn-00bb9f58)

~~~json
{
  "source": "00bb9f58",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f60`](#insn-00bb9f60)

~~~json
{
  "source": "00bb9f60",
  "target": "00bb9e70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f68`](#insn-00bb9f68)

~~~json
{
  "source": "00bb9f68",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f70`](#insn-00bb9f70)

~~~json
{
  "source": "00bb9f70",
  "target": "00bb9e78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f78`](#insn-00bb9f78)

~~~json
{
  "source": "00bb9f78",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f80`](#insn-00bb9f80)

~~~json
{
  "source": "00bb9f80",
  "target": "00bb9e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f88`](#insn-00bb9f88)

~~~json
{
  "source": "00bb9f88",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9f90`](#insn-00bb9f90)

~~~json
{
  "source": "00bb9f90",
  "target": "00bb9e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9f98`](#insn-00bb9f98)

~~~json
{
  "source": "00bb9f98",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9fa0`](#insn-00bb9fa0)

~~~json
{
  "source": "00bb9fa0",
  "target": "00bb9e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9fa8`](#insn-00bb9fa8)

~~~json
{
  "source": "00bb9fa8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9fb0`](#insn-00bb9fb0)

~~~json
{
  "source": "00bb9fb0",
  "target": "00bb9e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9fb8`](#insn-00bb9fb8)

~~~json
{
  "source": "00bb9fb8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9fc0`](#insn-00bb9fc0)

~~~json
{
  "source": "00bb9fc0",
  "target": "00bb9ea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9fc8`](#insn-00bb9fc8)

~~~json
{
  "source": "00bb9fc8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9fd0`](#insn-00bb9fd0)

~~~json
{
  "source": "00bb9fd0",
  "target": "00bb9ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9fd8`](#insn-00bb9fd8)

~~~json
{
  "source": "00bb9fd8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9fe0`](#insn-00bb9fe0)

~~~json
{
  "source": "00bb9fe0",
  "target": "00bb9eb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9fe8`](#insn-00bb9fe8)

~~~json
{
  "source": "00bb9fe8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9ff0`](#insn-00bb9ff0)

~~~json
{
  "source": "00bb9ff0",
  "target": "00bb9eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9ff8`](#insn-00bb9ff8)

~~~json
{
  "source": "00bb9ff8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba000`](#insn-00bba000)

~~~json
{
  "source": "00bba000",
  "target": "00bb9ec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba004`](#insn-00bba004)

~~~json
{
  "source": "00bba004",
  "target": "00bb9ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
