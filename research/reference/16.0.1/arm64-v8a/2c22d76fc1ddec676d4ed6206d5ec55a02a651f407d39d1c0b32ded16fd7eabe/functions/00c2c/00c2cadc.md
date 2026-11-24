# 00c2cadc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2c6b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0089.md#compare-53d30ff1d8e6869f55ec869c5f048a3c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c2cb78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0089.md#compare-0e647e0712348d71919d9f697ef3765d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2cadc",
  "name": "FUN_00c2cadc",
  "size": 1080,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "020e6a385ab5f902b8fd23c87f5c382ed20364eb8c5e69784bc6c3d728e9890e",
  "source_text_sha256": "020e6a385ab5f902b8fd23c87f5c382ed20364eb8c5e69784bc6c3d728e9890e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2cadc",
        "00c2cf13"
      ]
    ],
    "bytes_sha256": "0b7c3c43f5977ccd5631aa93239d20d3b24aaca48bdd85009012f1d9f9384978",
    "instruction_count": 270,
    "instruction_bytes": 1080,
    "body_bytes": 1080,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c2ca70](../00c2c/00c2ca70.md)

## 呼び出し先

- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

## 関連文字列（未確認候補）

~~~text
"Wednesday"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6936 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00c2cadc(void)

{
  undefined8 uVar1;
  int iVar2;
  char *pcVar3;
  undefined8 *puVar4;
  undefined4 *puVar5;
  
                    /* try { // try from 00c2caf4 to 00d2caff has its CatchHandler @ 00c2ccd4 */
  if (((DAT_011280f8 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_011280f8), iVar2 != 0)) {
    __cxa_atexit(FUN_00c35ba0,0,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_011280f8);
  }
  if ((DAT_01127fa8 & 1) == 0) {
    DAT_01127fa8 = 0xc;
    puVar5 = &DAT_01127fa9;
  }
  else {
    DAT_01127fb0 = 6;
    puVar5 = DAT_01127fb8;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e7553;
  if ((DAT_01127fc0 & 1) == 0) {
    DAT_01127fc0 = 0xc;
    puVar5 = &DAT_01127fc1;
  }
  else {
    DAT_01127fc8 = 6;
    puVar5 = DAT_01127fd0;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e6f4d;
  if ((DAT_01127fd8 & 1) == 0) {
                    /* try { // try from 00c2cba8 to 00d2cbab has its CatchHandler @ 00c2cd90 */
    DAT_01127fd8 = 0xe;
    puVar5 = &DAT_01127fd9;
  }
  else {
    DAT_01127fe0 = 7;
    puVar5 = DAT_01127fe8;
  }
  *(undefined1 *)((long)puVar5 + 7) = 0;
                    /* try { // try from 00c2cbd4 to 00d2cbdf has its CatchHandler @ 00c2ccb0 */
  *(undefined4 *)((long)puVar5 + 3) = 0x79616473;
                    /* try { // try from 00c2cbe0 to 00d2cbeb has its CatchHandler @ 00c2cc98 */
  *puVar5 = 0x73657554;
  uVar1 = s_Wednesday_002b8d72._0_8_;
  if ((DAT_01127ff0 & 1) == 0) {
    DAT_01127ff0 = 0x12;
    pcVar3 = (char *)&DAT_01127ff1;
  }
  else {
    ram0x01127ff8 = 9;
    pcVar3 = DAT_01128000;
  }
  pcVar3[8] = 'y';
  pcVar3[9] = '\0';
  *(undefined8 *)pcVar3 = uVar1;
                    /* try { // try from 00c2cc30 to 00d2cc37 has its CatchHandler @ 00c2cde0 */
  if ((DAT_01128008 & 1) == 0) {
    DAT_01128008 = 0x10;
    puVar4 = &DAT_01128009;
                    /* try { // try from 00c2cc48 to 00d2cc67 has its CatchHandler @ 00c2cddc */
  }
  else {
    ram0x01128010 = 8;
    puVar4 = DAT_01128018;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7961647372756854;
                    /* try { // try from 00c2cc78 to 00d2cc7f has its CatchHandler @ 00c2cd9c */
  if ((DAT_01128020 & 1) == 0) {
                    /* try { // try from 00c2cc90 to 00d2cc97 has its CatchHandler @ 00c2cd2c */
    DAT_01128020 = 0xc;
    puVar5 = &DAT_01128021;
  }
  else {
                    /* catch() { ... } // from try @ 00c2cbe0 with catch @ 00c2cc98
                       try { // try from 00c2cc98 to 00d2ce47 has its CatchHandler @ 00c2c450 */
    DAT_01128028 = 6;
    puVar5 = DAT_01128030;
  }
                    /* catch() { ... } // from try @ 00c2cbd4 with catch @ 00c2ccb0 */
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
                    /* catch() { ... } // from try @ 00c2ca74 with catch @ 00c2ccc0 */
  *puVar5 = 0x64697246;
  if ((DAT_01128038 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2caf4 with catch @ 00c2ccd4 */
                    /* catch() { ... } // from try @ 00c2cab4 with catch @ 00c2ccdc */
    DAT_01128038 = 0x10;
    puVar4 = &DAT_01128039;
  }
  else {
    ram0x01128040 = 8;
    puVar4 = DAT_01128048;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
                    /* catch() { ... } // from try @ 00c2ca2c with catch @ 00c2cd0c */
  *puVar4 = 0x7961647275746153;
                    /* catch() { ... } // from try @ 00c2c8ac with catch @ 00c2cd10 */
                    /* catch() { ... } // from try @ 00c2c908 with catch @ 00c2cd14 */
                    /* catch() { ... } // from try @ 00c2c880 with catch @ 00c2cd18 */
  if ((DAT_01128050 & 1) == 0) {
    DAT_01128050 = 6;
    puVar5 = &DAT_01128051;
                    /* catch() { ... } // from try @ 00c2c7fc with catch @ 00c2cd2c
                       catch() { ... } // from try @ 00c2cc90 with catch @ 00c2cd2c */
  }
  else {
                    /* catch() { ... } // from try @ 00c2c840 with catch @ 00c2cd34 */
    DAT_01128058 = 3;
    puVar5 = DAT_01128060;
  }
                    /* catch() { ... } // from try @ 00c2c6a0 with catch @ 00c2cd48 */
  *puVar5 = 0x6e7553;
  if ((DAT_01128068 & 1) == 0) {
    DAT_01128068 = 6;
    puVar5 = &DAT_01128069;
  }
  else {
                    /* catch() { ... } // from try @ 00c2c66c with catch @ 00c2cd80 */
    DAT_01128070 = 3;
    puVar5 = DAT_01128078;
  }
  *puVar5 = 0x6e6f4d;
                    /* catch() { ... } // from try @ 00c2c8e4 with catch @ 00c2cd90
                       catch() { ... } // from try @ 00c2cba8 with catch @ 00c2cd90 */
                    /* catch() { ... } // from try @ 00c2c738 with catch @ 00c2cd98 */
  if ((DAT_01128080 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2c6e8 with catch @ 00c2cd9c
                       catch() { ... } // from try @ 00c2cc78 with catch @ 00c2cd9c */
                    /* catch() { ... } // from try @ 00c2c630 with catch @ 00c2cda4 */
    DAT_01128080 = 6;
    puVar5 = &DAT_01128081;
  }
  else {
                    /* catch() { ... } // from try @ 00c2c5a0 with catch @ 00c2cdb8 */
    DAT_01128088 = 3;
    puVar5 = DAT_01128090;
  }
                    /* catch() { ... } // from try @ 00c2c4b8 with catch @ 00c2cdc8 */
  *puVar5 = 0x657554;
  if ((DAT_01128098 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2cc48 with catch @ 00c2cddc */
                    /* catch() { ... } // from try @ 00c2c560 with catch @ 00c2cde0
                       catch() { ... } // from try @ 00c2cc30 with catch @ 00c2cde0 */
                    /* catch() { ... } // from try @ 00c2c958 with catch @ 00c2cde8 */
    DAT_01128098 = 6;
    puVar5 = &DAT_01128099;
  }
  else {
    DAT_011280a0 = 3;
    puVar5 = DAT_011280a8;
  }
  *puVar5 = 0x646557;
  if ((DAT_011280b0 & 1) == 0) {
    DAT_011280b0 = 6;
    puVar5 = &DAT_011280b1;
  }
  else {
    DAT_011280b8 = 3;
    puVar5 = DAT_011280c0;
  }
                    /* try { // try from 00c2ce48 to 00d2ceb3 has its CatchHandler @ 00c2ce48
                       catch() { ... } // from try @ 00c2ce48 with catch @ 00c2ce48
                       catch() { ... } // from try @ 00c2cec4 with catch @ 00c2ce48 */
  *puVar5 = 0x756854;
  if ((DAT_011280c8 & 1) == 0) {
    DAT_011280c8 = 6;
    puVar5 = &DAT_011280c9;
  }
  else {
    DAT_011280d0 = 3;
    puVar5 = DAT_011280d8;
  }
  *puVar5 = 0x697246;
  if ((DAT_011280e0 & 1) == 0) {
    DAT_011280e0 = 6;
    puVar5 = &DAT_011280e1;
  }
  else {
                    /* try { // try from 00c2ceb4 to 00d2cec3 has its CatchHandler @ 00c2d218 */
    DAT_011280e8 = 3;
    puVar5 = DAT_011280f0;
  }
                    /* try { // try from 00c2cec4 to 00d2d257 has its CatchHandler @ 00c2ce48 */
  *puVar5 = 0x746153;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2cadc"></a> `00c2cadc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c2cae0"></a> `00c2cae0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00c2cae4"></a> `00c2cae4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c2cae8"></a> `00c2cae8` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2caec"></a> `00c2caec` | `08 e1 03 91` | add x8,x8,#0xf8 | `FALL_THROUGH`
<a id="insn-00c2caf0"></a> `00c2caf0` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00c2caf4"></a> `00c2caf4` | `48 1f 00 36` | tbz w8,#0x0,0x00c2cedc | `CONDITIONAL_JUMP`
<a id="insn-00c2caf8"></a> `00c2caf8` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cafc"></a> `00c2cafc` | `08 a1 7e 39` | ldrb w8,[x8, #0xfa8] | `FALL_THROUGH`
<a id="insn-00c2cb00"></a> `00c2cb00` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cb18 | `CONDITIONAL_JUMP`
<a id="insn-00c2cb04"></a> `00c2cb04` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb08"></a> `00c2cb08` | `08 a1 3e 91` | add x8,x8,#0xfa8 | `FALL_THROUGH`
<a id="insn-00c2cb0c"></a> `00c2cb0c` | `89 01 80 52` | mov w9,#0xc | `FALL_THROUGH`
<a id="insn-00c2cb10"></a> `00c2cb10` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cb14"></a> `00c2cb14` | `06 00 00 14` | b 0x00c2cb2c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cb18"></a> `00c2cb18` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb1c"></a> `00c2cb1c` | `29 c1 3e 91` | add x9,x9,#0xfb0 | `FALL_THROUGH`
<a id="insn-00c2cb20"></a> `00c2cb20` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cb24"></a> `00c2cb24` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cb28"></a> `00c2cb28` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cb2c"></a> `00c2cb2c` | `6a aa 8e 52` | mov w10,#0x7553 | `FALL_THROUGH`
<a id="insn-00c2cb30"></a> `00c2cb30` | `29 2c 8f 52` | mov w9,#0x7961 | `FALL_THROUGH`
<a id="insn-00c2cb34"></a> `00c2cb34` | `1f 19 00 39` | strb wzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00c2cb38"></a> `00c2cb38` | `ca 8d ac 72` | movk w10,#0x646e, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cb3c"></a> `00c2cb3c` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00c2cb40"></a> `00c2cb40` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb44"></a> `00c2cb44` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00c2cb48"></a> `00c2cb48` | `28 01 7f 39` | ldrb w8,[x9, #0xfc0] | `FALL_THROUGH`
<a id="insn-00c2cb4c"></a> `00c2cb4c` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cb64 | `CONDITIONAL_JUMP`
<a id="insn-00c2cb50"></a> `00c2cb50` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb54"></a> `00c2cb54` | `08 01 3f 91` | add x8,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00c2cb58"></a> `00c2cb58` | `89 01 80 52` | mov w9,#0xc | `FALL_THROUGH`
<a id="insn-00c2cb5c"></a> `00c2cb5c` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cb60"></a> `00c2cb60` | `06 00 00 14` | b 0x00c2cb78 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cb64"></a> `00c2cb64` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb68"></a> `00c2cb68` | `29 21 3f 91` | add x9,x9,#0xfc8 | `FALL_THROUGH`
<a id="insn-00c2cb6c"></a> `00c2cb6c` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cb70"></a> `00c2cb70` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cb74"></a> `00c2cb74` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cb78"></a> `00c2cb78` | `aa e9 8d 52` | mov w10,#0x6f4d | `FALL_THROUGH`
<a id="insn-00c2cb7c"></a> `00c2cb7c` | `29 2c 8f 52` | mov w9,#0x7961 | `FALL_THROUGH`
<a id="insn-00c2cb80"></a> `00c2cb80` | `1f 19 00 39` | strb wzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00c2cb84"></a> `00c2cb84` | `ca 8d ac 72` | movk w10,#0x646e, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cb88"></a> `00c2cb88` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00c2cb8c"></a> `00c2cb8c` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cb90"></a> `00c2cb90` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00c2cb94"></a> `00c2cb94` | `28 61 7f 39` | ldrb w8,[x9, #0xfd8] | `FALL_THROUGH`
<a id="insn-00c2cb98"></a> `00c2cb98` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cbb0 | `CONDITIONAL_JUMP`
<a id="insn-00c2cb9c"></a> `00c2cb9c` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cba0"></a> `00c2cba0` | `08 61 3f 91` | add x8,x8,#0xfd8 | `FALL_THROUGH`
<a id="insn-00c2cba4"></a> `00c2cba4` | `c9 01 80 52` | mov w9,#0xe | `FALL_THROUGH`
<a id="insn-00c2cba8"></a> `00c2cba8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cbac"></a> `00c2cbac` | `06 00 00 14` | b 0x00c2cbc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cbb0"></a> `00c2cbb0` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cbb4"></a> `00c2cbb4` | `29 81 3f 91` | add x9,x9,#0xfe0 | `FALL_THROUGH`
<a id="insn-00c2cbb8"></a> `00c2cbb8` | `ea 00 80 52` | mov w10,#0x7 | `FALL_THROUGH`
<a id="insn-00c2cbbc"></a> `00c2cbbc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cbc0"></a> `00c2cbc0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cbc4"></a> `00c2cbc4` | `69 8e 8c 52` | mov w9,#0x6473 | `FALL_THROUGH`
<a id="insn-00c2cbc8"></a> `00c2cbc8` | `8a aa 8e 52` | mov w10,#0x7554 | `FALL_THROUGH`
<a id="insn-00c2cbcc"></a> `00c2cbcc` | `1f 1d 00 39` | strb wzr,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00c2cbd0"></a> `00c2cbd0` | `29 2c af 72` | movk w9,#0x7961, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cbd4"></a> `00c2cbd4` | `aa 6c ae 72` | movk w10,#0x7365, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cbd8"></a> `00c2cbd8` | `09 31 00 b8` | stur w9,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00c2cbdc"></a> `00c2cbdc` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cbe0"></a> `00c2cbe0` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00c2cbe4"></a> `00c2cbe4` | `28 c1 7f 39` | ldrb w8,[x9, #0xff0] | `FALL_THROUGH`
<a id="insn-00c2cbe8"></a> `00c2cbe8` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cc00 | `CONDITIONAL_JUMP`
<a id="insn-00c2cbec"></a> `00c2cbec` | `c8 27 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cbf0"></a> `00c2cbf0` | `08 c1 3f 91` | add x8,x8,#0xff0 | `FALL_THROUGH`
<a id="insn-00c2cbf4"></a> `00c2cbf4` | `49 02 80 52` | mov w9,#0x12 | `FALL_THROUGH`
<a id="insn-00c2cbf8"></a> `00c2cbf8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cbfc"></a> `00c2cbfc` | `06 00 00 14` | b 0x00c2cc14 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cc00"></a> `00c2cc00` | `c9 27 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00c2cc04"></a> `00c2cc04` | `29 e1 3f 91` | add x9,x9,#0xff8 | `FALL_THROUGH`
<a id="insn-00c2cc08"></a> `00c2cc08` | `2a 01 80 52` | mov w10,#0x9 | `FALL_THROUGH`
<a id="insn-00c2cc0c"></a> `00c2cc0c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cc10"></a> `00c2cc10` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cc14"></a> `00c2cc14` | `6a b4 ff 90` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00c2cc18"></a> `00c2cc18` | `4a c9 35 91` | add x10,x10,#0xd72 | `FALL_THROUGH`
<a id="insn-00c2cc1c"></a> `00c2cc1c` | `29 0f 80 52` | mov w9,#0x79 | `FALL_THROUGH`
<a id="insn-00c2cc20"></a> `00c2cc20` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00c2cc24"></a> `00c2cc24` | `09 11 00 79` | strh w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cc28"></a> `00c2cc28` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00c2cc2c"></a> `00c2cc2c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cc30"></a> `00c2cc30` | `08 21 40 39` | ldrb w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cc34"></a> `00c2cc34` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cc4c | `CONDITIONAL_JUMP`
<a id="insn-00c2cc38"></a> `00c2cc38` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cc3c"></a> `00c2cc3c` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00c2cc40"></a> `00c2cc40` | `09 02 80 52` | mov w9,#0x10 | `FALL_THROUGH`
<a id="insn-00c2cc44"></a> `00c2cc44` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cc48"></a> `00c2cc48` | `06 00 00 14` | b 0x00c2cc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cc4c"></a> `00c2cc4c` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cc50"></a> `00c2cc50` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00c2cc54"></a> `00c2cc54` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00c2cc58"></a> `00c2cc58` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cc5c"></a> `00c2cc5c` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cc60"></a> `00c2cc60` | `89 0a 8d d2` | mov x9,#0x6854 | `FALL_THROUGH`
<a id="insn-00c2cc64"></a> `00c2cc64` | `1f 21 00 39` | strb wzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cc68"></a> `00c2cc68` | `a9 4e ae f2` | movk x9,#0x7275, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cc6c"></a> `00c2cc6c` | `69 8e cc f2` | movk x9,#0x6473, LSL #32 | `FALL_THROUGH`
<a id="insn-00c2cc70"></a> `00c2cc70` | `29 2c ef f2` | movk x9,#0x7961, LSL #48 | `FALL_THROUGH`
<a id="insn-00c2cc74"></a> `00c2cc74` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00c2cc78"></a> `00c2cc78` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cc7c"></a> `00c2cc7c` | `08 81 40 39` | ldrb w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c2cc80"></a> `00c2cc80` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cc98 | `CONDITIONAL_JUMP`
<a id="insn-00c2cc84"></a> `00c2cc84` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cc88"></a> `00c2cc88` | `08 81 00 91` | add x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c2cc8c"></a> `00c2cc8c` | `89 01 80 52` | mov w9,#0xc | `FALL_THROUGH`
<a id="insn-00c2cc90"></a> `00c2cc90` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cc94"></a> `00c2cc94` | `06 00 00 14` | b 0x00c2ccac | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cc98"></a> `00c2cc98` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cc9c"></a> `00c2cc9c` | `29 a1 00 91` | add x9,x9,#0x28 | `FALL_THROUGH`
<a id="insn-00c2cca0"></a> `00c2cca0` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cca4"></a> `00c2cca4` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cca8"></a> `00c2cca8` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2ccac"></a> `00c2ccac` | `ca 48 8e 52` | mov w10,#0x7246 | `FALL_THROUGH`
<a id="insn-00c2ccb0"></a> `00c2ccb0` | `29 2c 8f 52` | mov w9,#0x7961 | `FALL_THROUGH`
<a id="insn-00c2ccb4"></a> `00c2ccb4` | `1f 19 00 39` | strb wzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00c2ccb8"></a> `00c2ccb8` | `2a 8d ac 72` | movk w10,#0x6469, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2ccbc"></a> `00c2ccbc` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00c2ccc0"></a> `00c2ccc0` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ccc4"></a> `00c2ccc4` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00c2ccc8"></a> `00c2ccc8` | `28 e1 40 39` | ldrb w8,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-00c2cccc"></a> `00c2cccc` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cce4 | `CONDITIONAL_JUMP`
<a id="insn-00c2ccd0"></a> `00c2ccd0` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ccd4"></a> `00c2ccd4` | `08 e1 00 91` | add x8,x8,#0x38 | `FALL_THROUGH`
<a id="insn-00c2ccd8"></a> `00c2ccd8` | `09 02 80 52` | mov w9,#0x10 | `FALL_THROUGH`
<a id="insn-00c2ccdc"></a> `00c2ccdc` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cce0"></a> `00c2cce0` | `06 00 00 14` | b 0x00c2ccf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cce4"></a> `00c2cce4` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cce8"></a> `00c2cce8` | `29 01 01 91` | add x9,x9,#0x40 | `FALL_THROUGH`
<a id="insn-00c2ccec"></a> `00c2ccec` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00c2ccf0"></a> `00c2ccf0` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2ccf4"></a> `00c2ccf4` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2ccf8"></a> `00c2ccf8` | `69 2a 8c d2` | mov x9,#0x6153 | `FALL_THROUGH`
<a id="insn-00c2ccfc"></a> `00c2ccfc` | `1f 21 00 39` | strb wzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cd00"></a> `00c2cd00` | `89 ae ae f2` | movk x9,#0x7574, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cd04"></a> `00c2cd04` | `49 8e cc f2` | movk x9,#0x6472, LSL #32 | `FALL_THROUGH`
<a id="insn-00c2cd08"></a> `00c2cd08` | `29 2c ef f2` | movk x9,#0x7961, LSL #48 | `FALL_THROUGH`
<a id="insn-00c2cd0c"></a> `00c2cd0c` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00c2cd10"></a> `00c2cd10` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd14"></a> `00c2cd14` | `08 41 41 39` | ldrb w8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00c2cd18"></a> `00c2cd18` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cd30 | `CONDITIONAL_JUMP`
<a id="insn-00c2cd1c"></a> `00c2cd1c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd20"></a> `00c2cd20` | `08 41 01 91` | add x8,x8,#0x50 | `FALL_THROUGH`
<a id="insn-00c2cd24"></a> `00c2cd24` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cd28"></a> `00c2cd28` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cd2c"></a> `00c2cd2c` | `06 00 00 14` | b 0x00c2cd44 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cd30"></a> `00c2cd30` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd34"></a> `00c2cd34` | `29 61 01 91` | add x9,x9,#0x58 | `FALL_THROUGH`
<a id="insn-00c2cd38"></a> `00c2cd38` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2cd3c"></a> `00c2cd3c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cd40"></a> `00c2cd40` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cd44"></a> `00c2cd44` | `69 aa 8e 52` | mov w9,#0x7553 | `FALL_THROUGH`
<a id="insn-00c2cd48"></a> `00c2cd48` | `c9 0d a0 72` | movk w9,#0x6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cd4c"></a> `00c2cd4c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2cd50"></a> `00c2cd50` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd54"></a> `00c2cd54` | `08 a1 41 39` | ldrb w8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00c2cd58"></a> `00c2cd58` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cd70 | `CONDITIONAL_JUMP`
<a id="insn-00c2cd5c"></a> `00c2cd5c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd60"></a> `00c2cd60` | `08 a1 01 91` | add x8,x8,#0x68 | `FALL_THROUGH`
<a id="insn-00c2cd64"></a> `00c2cd64` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cd68"></a> `00c2cd68` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cd6c"></a> `00c2cd6c` | `06 00 00 14` | b 0x00c2cd84 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cd70"></a> `00c2cd70` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd74"></a> `00c2cd74` | `29 c1 01 91` | add x9,x9,#0x70 | `FALL_THROUGH`
<a id="insn-00c2cd78"></a> `00c2cd78` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2cd7c"></a> `00c2cd7c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cd80"></a> `00c2cd80` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cd84"></a> `00c2cd84` | `a9 e9 8d 52` | mov w9,#0x6f4d | `FALL_THROUGH`
<a id="insn-00c2cd88"></a> `00c2cd88` | `c9 0d a0 72` | movk w9,#0x6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cd8c"></a> `00c2cd8c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2cd90"></a> `00c2cd90` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cd94"></a> `00c2cd94` | `08 01 42 39` | ldrb w8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00c2cd98"></a> `00c2cd98` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cdb0 | `CONDITIONAL_JUMP`
<a id="insn-00c2cd9c"></a> `00c2cd9c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cda0"></a> `00c2cda0` | `08 01 02 91` | add x8,x8,#0x80 | `FALL_THROUGH`
<a id="insn-00c2cda4"></a> `00c2cda4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cda8"></a> `00c2cda8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cdac"></a> `00c2cdac` | `06 00 00 14` | b 0x00c2cdc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cdb0"></a> `00c2cdb0` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cdb4"></a> `00c2cdb4` | `29 21 02 91` | add x9,x9,#0x88 | `FALL_THROUGH`
<a id="insn-00c2cdb8"></a> `00c2cdb8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2cdbc"></a> `00c2cdbc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cdc0"></a> `00c2cdc0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cdc4"></a> `00c2cdc4` | `89 aa 8e 52` | mov w9,#0x7554 | `FALL_THROUGH`
<a id="insn-00c2cdc8"></a> `00c2cdc8` | `a9 0c a0 72` | movk w9,#0x65, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cdcc"></a> `00c2cdcc` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2cdd0"></a> `00c2cdd0` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cdd4"></a> `00c2cdd4` | `08 61 42 39` | ldrb w8,[x8, #0x98] | `FALL_THROUGH`
<a id="insn-00c2cdd8"></a> `00c2cdd8` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2cdf0 | `CONDITIONAL_JUMP`
<a id="insn-00c2cddc"></a> `00c2cddc` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cde0"></a> `00c2cde0` | `08 61 02 91` | add x8,x8,#0x98 | `FALL_THROUGH`
<a id="insn-00c2cde4"></a> `00c2cde4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cde8"></a> `00c2cde8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2cdec"></a> `00c2cdec` | `06 00 00 14` | b 0x00c2ce04 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2cdf0"></a> `00c2cdf0` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cdf4"></a> `00c2cdf4` | `29 81 02 91` | add x9,x9,#0xa0 | `FALL_THROUGH`
<a id="insn-00c2cdf8"></a> `00c2cdf8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2cdfc"></a> `00c2cdfc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2ce00"></a> `00c2ce00` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2ce04"></a> `00c2ce04` | `e9 aa 8c 52` | mov w9,#0x6557 | `FALL_THROUGH`
<a id="insn-00c2ce08"></a> `00c2ce08` | `89 0c a0 72` | movk w9,#0x64, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2ce0c"></a> `00c2ce0c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2ce10"></a> `00c2ce10` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce14"></a> `00c2ce14` | `08 c1 42 39` | ldrb w8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00c2ce18"></a> `00c2ce18` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2ce30 | `CONDITIONAL_JUMP`
<a id="insn-00c2ce1c"></a> `00c2ce1c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce20"></a> `00c2ce20` | `08 c1 02 91` | add x8,x8,#0xb0 | `FALL_THROUGH`
<a id="insn-00c2ce24"></a> `00c2ce24` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2ce28"></a> `00c2ce28` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2ce2c"></a> `00c2ce2c` | `06 00 00 14` | b 0x00c2ce44 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2ce30"></a> `00c2ce30` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce34"></a> `00c2ce34` | `29 e1 02 91` | add x9,x9,#0xb8 | `FALL_THROUGH`
<a id="insn-00c2ce38"></a> `00c2ce38` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2ce3c"></a> `00c2ce3c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2ce40"></a> `00c2ce40` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2ce44"></a> `00c2ce44` | `89 0a 8d 52` | mov w9,#0x6854 | `FALL_THROUGH`
<a id="insn-00c2ce48"></a> `00c2ce48` | `a9 0e a0 72` | movk w9,#0x75, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2ce4c"></a> `00c2ce4c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2ce50"></a> `00c2ce50` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce54"></a> `00c2ce54` | `08 21 43 39` | ldrb w8,[x8, #0xc8] | `FALL_THROUGH`
<a id="insn-00c2ce58"></a> `00c2ce58` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2ce70 | `CONDITIONAL_JUMP`
<a id="insn-00c2ce5c"></a> `00c2ce5c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce60"></a> `00c2ce60` | `08 21 03 91` | add x8,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00c2ce64"></a> `00c2ce64` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2ce68"></a> `00c2ce68` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2ce6c"></a> `00c2ce6c` | `06 00 00 14` | b 0x00c2ce84 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2ce70"></a> `00c2ce70` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce74"></a> `00c2ce74` | `29 41 03 91` | add x9,x9,#0xd0 | `FALL_THROUGH`
<a id="insn-00c2ce78"></a> `00c2ce78` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2ce7c"></a> `00c2ce7c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2ce80"></a> `00c2ce80` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2ce84"></a> `00c2ce84` | `c9 48 8e 52` | mov w9,#0x7246 | `FALL_THROUGH`
<a id="insn-00c2ce88"></a> `00c2ce88` | `29 0d a0 72` | movk w9,#0x69, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2ce8c"></a> `00c2ce8c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2ce90"></a> `00c2ce90` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ce94"></a> `00c2ce94` | `08 81 43 39` | ldrb w8,[x8, #0xe0] | `FALL_THROUGH`
<a id="insn-00c2ce98"></a> `00c2ce98` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2ceb0 | `CONDITIONAL_JUMP`
<a id="insn-00c2ce9c"></a> `00c2ce9c` | `e8 27 00 90` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cea0"></a> `00c2cea0` | `08 81 03 91` | add x8,x8,#0xe0 | `FALL_THROUGH`
<a id="insn-00c2cea4"></a> `00c2cea4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00c2cea8"></a> `00c2cea8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2ceac"></a> `00c2ceac` | `06 00 00 14` | b 0x00c2cec4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c2ceb0"></a> `00c2ceb0` | `e9 27 00 90` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2ceb4"></a> `00c2ceb4` | `29 a1 03 91` | add x9,x9,#0xe8 | `FALL_THROUGH`
<a id="insn-00c2ceb8"></a> `00c2ceb8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00c2cebc"></a> `00c2cebc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2cec0"></a> `00c2cec0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2cec4"></a> `00c2cec4` | `69 2a 8c 52` | mov w9,#0x6153 | `FALL_THROUGH`
<a id="insn-00c2cec8"></a> `00c2cec8` | `89 0e a0 72` | movk w9,#0x74, LSL #16 | `FALL_THROUGH`
<a id="insn-00c2cecc"></a> `00c2cecc` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2ced0"></a> `00c2ced0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00c2ced4"></a> `00c2ced4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c2ced8"></a> `00c2ced8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c2cedc"></a> `00c2cedc` | `e0 27 00 90` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cee0"></a> `00c2cee0` | `00 e0 03 91` | add x0,x0,#0xf8 | `FALL_THROUGH`
<a id="insn-00c2cee4"></a> `00c2cee4` | `db ab 00 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00c2cee8"></a> `00c2cee8` | `80 e0 ff 34` | cbz w0,0x00c2caf8 | `CONDITIONAL_JUMP`
<a id="insn-00c2ceec"></a> `00c2ceec` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c2cef0"></a> `00c2cef0` | `80 65 04 10` | adr x0,0xc35ba0 | `FALL_THROUGH`
<a id="insn-00c2cef4"></a> `00c2cef4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c2cef8"></a> `00c2cef8` | `c2 04 1b 10` | adr x2,0xc62f90 | `FALL_THROUGH`
<a id="insn-00c2cefc"></a> `00c2cefc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00c2cf00"></a> `00c2cf00` | `cc ab 00 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00c2cf04"></a> `00c2cf04` | `e0 27 00 90` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2cf08"></a> `00c2cf08` | `00 e0 03 91` | add x0,x0,#0xf8 | `FALL_THROUGH`
<a id="insn-00c2cf0c"></a> `00c2cf0c` | `d9 ab 00 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00c2cf10"></a> `00c2cf10` | `fa fe ff 17` | b 0x00c2caf8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c2cadc`](#insn-00c2cadc) 範囲 `[['00c2cadc', '00c2caf3']]`
  - `FALL_THROUGH` [`00c2caf0`](#insn-00c2caf0) → [`00c2caf4`](#insn-00c2caf4)
- ブロック [`00c2caf4`](#insn-00c2caf4) 範囲 `[['00c2caf4', '00c2caf7']]`
  - `CONDITIONAL_JUMP` [`00c2caf4`](#insn-00c2caf4) → [`00c2cedc`](#insn-00c2cedc)
  - `FALL_THROUGH` [`00c2caf4`](#insn-00c2caf4) → [`00c2caf8`](#insn-00c2caf8)
- ブロック [`00c2caf8`](#insn-00c2caf8) 範囲 `[['00c2caf8', '00c2cb03']]`
  - `CONDITIONAL_JUMP` [`00c2cb00`](#insn-00c2cb00) → [`00c2cb18`](#insn-00c2cb18)
  - `FALL_THROUGH` [`00c2cb00`](#insn-00c2cb00) → [`00c2cb04`](#insn-00c2cb04)
- ブロック [`00c2cb04`](#insn-00c2cb04) 範囲 `[['00c2cb04', '00c2cb17']]`
  - `UNCONDITIONAL_JUMP` [`00c2cb14`](#insn-00c2cb14) → [`00c2cb2c`](#insn-00c2cb2c)
- ブロック [`00c2cb18`](#insn-00c2cb18) 範囲 `[['00c2cb18', '00c2cb2b']]`
  - `FALL_THROUGH` [`00c2cb28`](#insn-00c2cb28) → [`00c2cb2c`](#insn-00c2cb2c)
- ブロック [`00c2cb2c`](#insn-00c2cb2c) 範囲 `[['00c2cb2c', '00c2cb4f']]`
  - `CONDITIONAL_JUMP` [`00c2cb4c`](#insn-00c2cb4c) → [`00c2cb64`](#insn-00c2cb64)
  - `FALL_THROUGH` [`00c2cb4c`](#insn-00c2cb4c) → [`00c2cb50`](#insn-00c2cb50)
- ブロック [`00c2cb50`](#insn-00c2cb50) 範囲 `[['00c2cb50', '00c2cb63']]`
  - `UNCONDITIONAL_JUMP` [`00c2cb60`](#insn-00c2cb60) → [`00c2cb78`](#insn-00c2cb78)
- ブロック [`00c2cb64`](#insn-00c2cb64) 範囲 `[['00c2cb64', '00c2cb77']]`
  - `FALL_THROUGH` [`00c2cb74`](#insn-00c2cb74) → [`00c2cb78`](#insn-00c2cb78)
- ブロック [`00c2cb78`](#insn-00c2cb78) 範囲 `[['00c2cb78', '00c2cb9b']]`
  - `CONDITIONAL_JUMP` [`00c2cb98`](#insn-00c2cb98) → [`00c2cbb0`](#insn-00c2cbb0)
  - `FALL_THROUGH` [`00c2cb98`](#insn-00c2cb98) → [`00c2cb9c`](#insn-00c2cb9c)
- ブロック [`00c2cb9c`](#insn-00c2cb9c) 範囲 `[['00c2cb9c', '00c2cba7']]`
  - `FALL_THROUGH` [`00c2cba4`](#insn-00c2cba4) → [`00c2cba8`](#insn-00c2cba8)
- ブロック [`00c2cba8`](#insn-00c2cba8) 範囲 `[['00c2cba8', '00c2cbaf']]`
  - `UNCONDITIONAL_JUMP` [`00c2cbac`](#insn-00c2cbac) → [`00c2cbc4`](#insn-00c2cbc4)
- ブロック [`00c2cbb0`](#insn-00c2cbb0) 範囲 `[['00c2cbb0', '00c2cbc3']]`
  - `FALL_THROUGH` [`00c2cbc0`](#insn-00c2cbc0) → [`00c2cbc4`](#insn-00c2cbc4)
- ブロック [`00c2cbc4`](#insn-00c2cbc4) 範囲 `[['00c2cbc4', '00c2cbd3']]`
  - `FALL_THROUGH` [`00c2cbd0`](#insn-00c2cbd0) → [`00c2cbd4`](#insn-00c2cbd4)
- ブロック [`00c2cbd4`](#insn-00c2cbd4) 範囲 `[['00c2cbd4', '00c2cbdf']]`
  - `FALL_THROUGH` [`00c2cbdc`](#insn-00c2cbdc) → [`00c2cbe0`](#insn-00c2cbe0)
- ブロック [`00c2cbe0`](#insn-00c2cbe0) 範囲 `[['00c2cbe0', '00c2cbeb']]`
  - `CONDITIONAL_JUMP` [`00c2cbe8`](#insn-00c2cbe8) → [`00c2cc00`](#insn-00c2cc00)
  - `FALL_THROUGH` [`00c2cbe8`](#insn-00c2cbe8) → [`00c2cbec`](#insn-00c2cbec)
- ブロック [`00c2cbec`](#insn-00c2cbec) 範囲 `[['00c2cbec', '00c2cbff']]`
  - `UNCONDITIONAL_JUMP` [`00c2cbfc`](#insn-00c2cbfc) → [`00c2cc14`](#insn-00c2cc14)
- ブロック [`00c2cc00`](#insn-00c2cc00) 範囲 `[['00c2cc00', '00c2cc13']]`
  - `FALL_THROUGH` [`00c2cc10`](#insn-00c2cc10) → [`00c2cc14`](#insn-00c2cc14)
- ブロック [`00c2cc14`](#insn-00c2cc14) 範囲 `[['00c2cc14', '00c2cc2f']]`
  - `FALL_THROUGH` [`00c2cc2c`](#insn-00c2cc2c) → [`00c2cc30`](#insn-00c2cc30)
- ブロック [`00c2cc30`](#insn-00c2cc30) 範囲 `[['00c2cc30', '00c2cc37']]`
  - `CONDITIONAL_JUMP` [`00c2cc34`](#insn-00c2cc34) → [`00c2cc4c`](#insn-00c2cc4c)
  - `FALL_THROUGH` [`00c2cc34`](#insn-00c2cc34) → [`00c2cc38`](#insn-00c2cc38)
- ブロック [`00c2cc38`](#insn-00c2cc38) 範囲 `[['00c2cc38', '00c2cc47']]`
  - `FALL_THROUGH` [`00c2cc44`](#insn-00c2cc44) → [`00c2cc48`](#insn-00c2cc48)
- ブロック [`00c2cc48`](#insn-00c2cc48) 範囲 `[['00c2cc48', '00c2cc4b']]`
  - `UNCONDITIONAL_JUMP` [`00c2cc48`](#insn-00c2cc48) → [`00c2cc60`](#insn-00c2cc60)
- ブロック [`00c2cc4c`](#insn-00c2cc4c) 範囲 `[['00c2cc4c', '00c2cc5f']]`
  - `FALL_THROUGH` [`00c2cc5c`](#insn-00c2cc5c) → [`00c2cc60`](#insn-00c2cc60)
- ブロック [`00c2cc60`](#insn-00c2cc60) 範囲 `[['00c2cc60', '00c2cc77']]`
  - `FALL_THROUGH` [`00c2cc74`](#insn-00c2cc74) → [`00c2cc78`](#insn-00c2cc78)
- ブロック [`00c2cc78`](#insn-00c2cc78) 範囲 `[['00c2cc78', '00c2cc83']]`
  - `CONDITIONAL_JUMP` [`00c2cc80`](#insn-00c2cc80) → [`00c2cc98`](#insn-00c2cc98)
  - `FALL_THROUGH` [`00c2cc80`](#insn-00c2cc80) → [`00c2cc84`](#insn-00c2cc84)
- ブロック [`00c2cc84`](#insn-00c2cc84) 範囲 `[['00c2cc84', '00c2cc8f']]`
  - `FALL_THROUGH` [`00c2cc8c`](#insn-00c2cc8c) → [`00c2cc90`](#insn-00c2cc90)
- ブロック [`00c2cc90`](#insn-00c2cc90) 範囲 `[['00c2cc90', '00c2cc97']]`
  - `UNCONDITIONAL_JUMP` [`00c2cc94`](#insn-00c2cc94) → [`00c2ccac`](#insn-00c2ccac)
- ブロック [`00c2cc98`](#insn-00c2cc98) 範囲 `[['00c2cc98', '00c2ccab']]`
  - `FALL_THROUGH` [`00c2cca8`](#insn-00c2cca8) → [`00c2ccac`](#insn-00c2ccac)
- ブロック [`00c2ccac`](#insn-00c2ccac) 範囲 `[['00c2ccac', '00c2ccaf']]`
  - `FALL_THROUGH` [`00c2ccac`](#insn-00c2ccac) → [`00c2ccb0`](#insn-00c2ccb0)
- ブロック [`00c2ccb0`](#insn-00c2ccb0) 範囲 `[['00c2ccb0', '00c2ccbf']]`
  - `FALL_THROUGH` [`00c2ccbc`](#insn-00c2ccbc) → [`00c2ccc0`](#insn-00c2ccc0)
- ブロック [`00c2ccc0`](#insn-00c2ccc0) 範囲 `[['00c2ccc0', '00c2cccf']]`
  - `CONDITIONAL_JUMP` [`00c2cccc`](#insn-00c2cccc) → [`00c2cce4`](#insn-00c2cce4)
  - `FALL_THROUGH` [`00c2cccc`](#insn-00c2cccc) → [`00c2ccd0`](#insn-00c2ccd0)
- ブロック [`00c2ccd0`](#insn-00c2ccd0) 範囲 `[['00c2ccd0', '00c2ccd3']]`
  - `FALL_THROUGH` [`00c2ccd0`](#insn-00c2ccd0) → [`00c2ccd4`](#insn-00c2ccd4)
- ブロック [`00c2ccd4`](#insn-00c2ccd4) 範囲 `[['00c2ccd4', '00c2ccdb']]`
  - `FALL_THROUGH` [`00c2ccd8`](#insn-00c2ccd8) → [`00c2ccdc`](#insn-00c2ccdc)
- ブロック [`00c2ccdc`](#insn-00c2ccdc) 範囲 `[['00c2ccdc', '00c2cce3']]`
  - `UNCONDITIONAL_JUMP` [`00c2cce0`](#insn-00c2cce0) → [`00c2ccf8`](#insn-00c2ccf8)
- ブロック [`00c2cce4`](#insn-00c2cce4) 範囲 `[['00c2cce4', '00c2ccf7']]`
  - `FALL_THROUGH` [`00c2ccf4`](#insn-00c2ccf4) → [`00c2ccf8`](#insn-00c2ccf8)
- ブロック [`00c2ccf8`](#insn-00c2ccf8) 範囲 `[['00c2ccf8', '00c2cd0b']]`
  - `FALL_THROUGH` [`00c2cd08`](#insn-00c2cd08) → [`00c2cd0c`](#insn-00c2cd0c)
- ブロック [`00c2cd0c`](#insn-00c2cd0c) 範囲 `[['00c2cd0c', '00c2cd0f']]`
  - `FALL_THROUGH` [`00c2cd0c`](#insn-00c2cd0c) → [`00c2cd10`](#insn-00c2cd10)
- ブロック [`00c2cd10`](#insn-00c2cd10) 範囲 `[['00c2cd10', '00c2cd13']]`
  - `FALL_THROUGH` [`00c2cd10`](#insn-00c2cd10) → [`00c2cd14`](#insn-00c2cd14)
- ブロック [`00c2cd14`](#insn-00c2cd14) 範囲 `[['00c2cd14', '00c2cd17']]`
  - `FALL_THROUGH` [`00c2cd14`](#insn-00c2cd14) → [`00c2cd18`](#insn-00c2cd18)
- ブロック [`00c2cd18`](#insn-00c2cd18) 範囲 `[['00c2cd18', '00c2cd1b']]`
  - `CONDITIONAL_JUMP` [`00c2cd18`](#insn-00c2cd18) → [`00c2cd30`](#insn-00c2cd30)
  - `FALL_THROUGH` [`00c2cd18`](#insn-00c2cd18) → [`00c2cd1c`](#insn-00c2cd1c)
- ブロック [`00c2cd1c`](#insn-00c2cd1c) 範囲 `[['00c2cd1c', '00c2cd2b']]`
  - `FALL_THROUGH` [`00c2cd28`](#insn-00c2cd28) → [`00c2cd2c`](#insn-00c2cd2c)
- ブロック [`00c2cd2c`](#insn-00c2cd2c) 範囲 `[['00c2cd2c', '00c2cd2f']]`
  - `UNCONDITIONAL_JUMP` [`00c2cd2c`](#insn-00c2cd2c) → [`00c2cd44`](#insn-00c2cd44)
- ブロック [`00c2cd30`](#insn-00c2cd30) 範囲 `[['00c2cd30', '00c2cd33']]`
  - `FALL_THROUGH` [`00c2cd30`](#insn-00c2cd30) → [`00c2cd34`](#insn-00c2cd34)
- ブロック [`00c2cd34`](#insn-00c2cd34) 範囲 `[['00c2cd34', '00c2cd43']]`
  - `FALL_THROUGH` [`00c2cd40`](#insn-00c2cd40) → [`00c2cd44`](#insn-00c2cd44)
- ブロック [`00c2cd44`](#insn-00c2cd44) 範囲 `[['00c2cd44', '00c2cd47']]`
  - `FALL_THROUGH` [`00c2cd44`](#insn-00c2cd44) → [`00c2cd48`](#insn-00c2cd48)
- ブロック [`00c2cd48`](#insn-00c2cd48) 範囲 `[['00c2cd48', '00c2cd5b']]`
  - `CONDITIONAL_JUMP` [`00c2cd58`](#insn-00c2cd58) → [`00c2cd70`](#insn-00c2cd70)
  - `FALL_THROUGH` [`00c2cd58`](#insn-00c2cd58) → [`00c2cd5c`](#insn-00c2cd5c)
- ブロック [`00c2cd5c`](#insn-00c2cd5c) 範囲 `[['00c2cd5c', '00c2cd6f']]`
  - `UNCONDITIONAL_JUMP` [`00c2cd6c`](#insn-00c2cd6c) → [`00c2cd84`](#insn-00c2cd84)
- ブロック [`00c2cd70`](#insn-00c2cd70) 範囲 `[['00c2cd70', '00c2cd7f']]`
  - `FALL_THROUGH` [`00c2cd7c`](#insn-00c2cd7c) → [`00c2cd80`](#insn-00c2cd80)
- ブロック [`00c2cd80`](#insn-00c2cd80) 範囲 `[['00c2cd80', '00c2cd83']]`
  - `FALL_THROUGH` [`00c2cd80`](#insn-00c2cd80) → [`00c2cd84`](#insn-00c2cd84)
- ブロック [`00c2cd84`](#insn-00c2cd84) 範囲 `[['00c2cd84', '00c2cd8f']]`
  - `FALL_THROUGH` [`00c2cd8c`](#insn-00c2cd8c) → [`00c2cd90`](#insn-00c2cd90)
- ブロック [`00c2cd90`](#insn-00c2cd90) 範囲 `[['00c2cd90', '00c2cd97']]`
  - `FALL_THROUGH` [`00c2cd94`](#insn-00c2cd94) → [`00c2cd98`](#insn-00c2cd98)
- ブロック [`00c2cd98`](#insn-00c2cd98) 範囲 `[['00c2cd98', '00c2cd9b']]`
  - `CONDITIONAL_JUMP` [`00c2cd98`](#insn-00c2cd98) → [`00c2cdb0`](#insn-00c2cdb0)
  - `FALL_THROUGH` [`00c2cd98`](#insn-00c2cd98) → [`00c2cd9c`](#insn-00c2cd9c)
- ブロック [`00c2cd9c`](#insn-00c2cd9c) 範囲 `[['00c2cd9c', '00c2cda3']]`
  - `FALL_THROUGH` [`00c2cda0`](#insn-00c2cda0) → [`00c2cda4`](#insn-00c2cda4)
- ブロック [`00c2cda4`](#insn-00c2cda4) 範囲 `[['00c2cda4', '00c2cdaf']]`
  - `UNCONDITIONAL_JUMP` [`00c2cdac`](#insn-00c2cdac) → [`00c2cdc4`](#insn-00c2cdc4)
- ブロック [`00c2cdb0`](#insn-00c2cdb0) 範囲 `[['00c2cdb0', '00c2cdb7']]`
  - `FALL_THROUGH` [`00c2cdb4`](#insn-00c2cdb4) → [`00c2cdb8`](#insn-00c2cdb8)
- ブロック [`00c2cdb8`](#insn-00c2cdb8) 範囲 `[['00c2cdb8', '00c2cdc3']]`
  - `FALL_THROUGH` [`00c2cdc0`](#insn-00c2cdc0) → [`00c2cdc4`](#insn-00c2cdc4)
- ブロック [`00c2cdc4`](#insn-00c2cdc4) 範囲 `[['00c2cdc4', '00c2cdc7']]`
  - `FALL_THROUGH` [`00c2cdc4`](#insn-00c2cdc4) → [`00c2cdc8`](#insn-00c2cdc8)
- ブロック [`00c2cdc8`](#insn-00c2cdc8) 範囲 `[['00c2cdc8', '00c2cddb']]`
  - `CONDITIONAL_JUMP` [`00c2cdd8`](#insn-00c2cdd8) → [`00c2cdf0`](#insn-00c2cdf0)
  - `FALL_THROUGH` [`00c2cdd8`](#insn-00c2cdd8) → [`00c2cddc`](#insn-00c2cddc)
- ブロック [`00c2cddc`](#insn-00c2cddc) 範囲 `[['00c2cddc', '00c2cddf']]`
  - `FALL_THROUGH` [`00c2cddc`](#insn-00c2cddc) → [`00c2cde0`](#insn-00c2cde0)
- ブロック [`00c2cde0`](#insn-00c2cde0) 範囲 `[['00c2cde0', '00c2cde7']]`
  - `FALL_THROUGH` [`00c2cde4`](#insn-00c2cde4) → [`00c2cde8`](#insn-00c2cde8)
- ブロック [`00c2cde8`](#insn-00c2cde8) 範囲 `[['00c2cde8', '00c2cdef']]`
  - `UNCONDITIONAL_JUMP` [`00c2cdec`](#insn-00c2cdec) → [`00c2ce04`](#insn-00c2ce04)
- ブロック [`00c2cdf0`](#insn-00c2cdf0) 範囲 `[['00c2cdf0', '00c2ce03']]`
  - `FALL_THROUGH` [`00c2ce00`](#insn-00c2ce00) → [`00c2ce04`](#insn-00c2ce04)
- ブロック [`00c2ce04`](#insn-00c2ce04) 範囲 `[['00c2ce04', '00c2ce1b']]`
  - `CONDITIONAL_JUMP` [`00c2ce18`](#insn-00c2ce18) → [`00c2ce30`](#insn-00c2ce30)
  - `FALL_THROUGH` [`00c2ce18`](#insn-00c2ce18) → [`00c2ce1c`](#insn-00c2ce1c)
- ブロック [`00c2ce1c`](#insn-00c2ce1c) 範囲 `[['00c2ce1c', '00c2ce2f']]`
  - `UNCONDITIONAL_JUMP` [`00c2ce2c`](#insn-00c2ce2c) → [`00c2ce44`](#insn-00c2ce44)
- ブロック [`00c2ce30`](#insn-00c2ce30) 範囲 `[['00c2ce30', '00c2ce43']]`
  - `FALL_THROUGH` [`00c2ce40`](#insn-00c2ce40) → [`00c2ce44`](#insn-00c2ce44)
- ブロック [`00c2ce44`](#insn-00c2ce44) 範囲 `[['00c2ce44', '00c2ce47']]`
  - `FALL_THROUGH` [`00c2ce44`](#insn-00c2ce44) → [`00c2ce48`](#insn-00c2ce48)
- ブロック [`00c2ce48`](#insn-00c2ce48) 範囲 `[['00c2ce48', '00c2ce5b']]`
  - `CONDITIONAL_JUMP` [`00c2ce58`](#insn-00c2ce58) → [`00c2ce70`](#insn-00c2ce70)
  - `FALL_THROUGH` [`00c2ce58`](#insn-00c2ce58) → [`00c2ce5c`](#insn-00c2ce5c)
- ブロック [`00c2ce5c`](#insn-00c2ce5c) 範囲 `[['00c2ce5c', '00c2ce6f']]`
  - `UNCONDITIONAL_JUMP` [`00c2ce6c`](#insn-00c2ce6c) → [`00c2ce84`](#insn-00c2ce84)
- ブロック [`00c2ce70`](#insn-00c2ce70) 範囲 `[['00c2ce70', '00c2ce83']]`
  - `FALL_THROUGH` [`00c2ce80`](#insn-00c2ce80) → [`00c2ce84`](#insn-00c2ce84)
- ブロック [`00c2ce84`](#insn-00c2ce84) 範囲 `[['00c2ce84', '00c2ce9b']]`
  - `CONDITIONAL_JUMP` [`00c2ce98`](#insn-00c2ce98) → [`00c2ceb0`](#insn-00c2ceb0)
  - `FALL_THROUGH` [`00c2ce98`](#insn-00c2ce98) → [`00c2ce9c`](#insn-00c2ce9c)
- ブロック [`00c2ce9c`](#insn-00c2ce9c) 範囲 `[['00c2ce9c', '00c2ceaf']]`
  - `UNCONDITIONAL_JUMP` [`00c2ceac`](#insn-00c2ceac) → [`00c2cec4`](#insn-00c2cec4)
- ブロック [`00c2ceb0`](#insn-00c2ceb0) 範囲 `[['00c2ceb0', '00c2ceb3']]`
  - `FALL_THROUGH` [`00c2ceb0`](#insn-00c2ceb0) → [`00c2ceb4`](#insn-00c2ceb4)
- ブロック [`00c2ceb4`](#insn-00c2ceb4) 範囲 `[['00c2ceb4', '00c2cec3']]`
  - `FALL_THROUGH` [`00c2cec0`](#insn-00c2cec0) → [`00c2cec4`](#insn-00c2cec4)
- ブロック [`00c2cec4`](#insn-00c2cec4) 範囲 `[['00c2cec4', '00c2cedb']]`
- ブロック [`00c2cedc`](#insn-00c2cedc) 範囲 `[['00c2cedc', '00c2ceeb']]`
  - `CONDITIONAL_JUMP` [`00c2cee8`](#insn-00c2cee8) → [`00c2caf8`](#insn-00c2caf8)
  - `FALL_THROUGH` [`00c2cee8`](#insn-00c2cee8) → [`00c2ceec`](#insn-00c2ceec)
- ブロック [`00c2ceec`](#insn-00c2ceec) 範囲 `[['00c2ceec', '00c2cf13']]`
  - `UNCONDITIONAL_JUMP` [`00c2cf10`](#insn-00c2cf10) → [`00c2caf8`](#insn-00c2caf8)

## 命令位置別の参照

- [`00c2cae0`](#insn-00c2cae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2caf0`](#insn-00c2caf0) → `011280f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2caf4`](#insn-00c2caf4) → [`00c2cedc`](#insn-00c2cedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cafc`](#insn-00c2cafc) → `01127fa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb00`](#insn-00c2cb00) → [`00c2cb18`](#insn-00c2cb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb10`](#insn-00c2cb10) → `01127fa8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb14`](#insn-00c2cb14) → [`00c2cb2c`](#insn-00c2cb2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb24`](#insn-00c2cb24) → `01127fb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cb28`](#insn-00c2cb28) → `01127fb0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cb34`](#insn-00c2cb34) → `01127faf`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb3c`](#insn-00c2cb3c) → `01127fad`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00c2cb44`](#insn-00c2cb44) → `01127fa9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cb48`](#insn-00c2cb48) → `01127fc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb4c`](#insn-00c2cb4c) → [`00c2cb64`](#insn-00c2cb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb5c`](#insn-00c2cb5c) → `01127fc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb60`](#insn-00c2cb60) → [`00c2cb78`](#insn-00c2cb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cb70`](#insn-00c2cb70) → `01127fd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cb74`](#insn-00c2cb74) → `01127fc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cb80`](#insn-00c2cb80) → `01127fc7`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb88`](#insn-00c2cb88) → `01127fc5`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00c2cb90`](#insn-00c2cb90) → `01127fc1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cb94`](#insn-00c2cb94) → `01127fd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cb98`](#insn-00c2cb98) → [`00c2cbb0`](#insn-00c2cbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cba8`](#insn-00c2cba8) → `01127fd8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cbac`](#insn-00c2cbac) → [`00c2cbc4`](#insn-00c2cbc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cbbc`](#insn-00c2cbbc) → `01127fe8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cbc0`](#insn-00c2cbc0) → `01127fe0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cbcc`](#insn-00c2cbcc) → `01127fe0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cbd8`](#insn-00c2cbd8) → `01127fdc`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cbe0`](#insn-00c2cbe0) → `01127fd9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cbe4`](#insn-00c2cbe4) → `01127ff0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cbe8`](#insn-00c2cbe8) → [`00c2cc00`](#insn-00c2cc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cbf8`](#insn-00c2cbf8) → `01127ff0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cbfc`](#insn-00c2cbfc) → [`00c2cc14`](#insn-00c2cc14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cc0c`](#insn-00c2cc0c) → `01128000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cc10`](#insn-00c2cc10) → `01127ff8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cc20`](#insn-00c2cc20) → `002b8d72`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c2cc24`](#insn-00c2cc24) → `01127ff9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00c2cc28`](#insn-00c2cc28) → `01127ff1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cc30`](#insn-00c2cc30) → `01128008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cc34`](#insn-00c2cc34) → [`00c2cc4c`](#insn-00c2cc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cc44`](#insn-00c2cc44) → `01128008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cc48`](#insn-00c2cc48) → [`00c2cc60`](#insn-00c2cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cc58`](#insn-00c2cc58) → `01128018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cc5c`](#insn-00c2cc5c) → `01128010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cc64`](#insn-00c2cc64) → `01128011`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cc74`](#insn-00c2cc74) → `01128009`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cc7c`](#insn-00c2cc7c) → `01128020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cc80`](#insn-00c2cc80) → [`00c2cc98`](#insn-00c2cc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cc90`](#insn-00c2cc90) → `01128020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cc94`](#insn-00c2cc94) → [`00c2ccac`](#insn-00c2ccac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cca4`](#insn-00c2cca4) → `01128030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cca8`](#insn-00c2cca8) → `01128028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ccb4`](#insn-00c2ccb4) → `01128027`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ccbc`](#insn-00c2ccbc) → `01128025`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00c2ccc4`](#insn-00c2ccc4) → `01128021`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2ccc8`](#insn-00c2ccc8) → `01128038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cccc`](#insn-00c2cccc) → [`00c2cce4`](#insn-00c2cce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ccdc`](#insn-00c2ccdc) → `01128038`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cce0`](#insn-00c2cce0) → [`00c2ccf8`](#insn-00c2ccf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ccf0`](#insn-00c2ccf0) → `01128048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ccf4`](#insn-00c2ccf4) → `01128040`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ccfc`](#insn-00c2ccfc) → `01128041`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cd0c`](#insn-00c2cd0c) → `01128039`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cd14`](#insn-00c2cd14) → `01128050`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cd18`](#insn-00c2cd18) → [`00c2cd30`](#insn-00c2cd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cd28`](#insn-00c2cd28) → `01128050`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cd2c`](#insn-00c2cd2c) → [`00c2cd44`](#insn-00c2cd44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cd3c`](#insn-00c2cd3c) → `01128060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cd40`](#insn-00c2cd40) → `01128058`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cd4c`](#insn-00c2cd4c) → `01128051`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cd54`](#insn-00c2cd54) → `01128068`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cd58`](#insn-00c2cd58) → [`00c2cd70`](#insn-00c2cd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cd68`](#insn-00c2cd68) → `01128068`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cd6c`](#insn-00c2cd6c) → [`00c2cd84`](#insn-00c2cd84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cd7c`](#insn-00c2cd7c) → `01128078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cd80`](#insn-00c2cd80) → `01128070`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cd8c`](#insn-00c2cd8c) → `01128069`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cd8c`](#insn-00c2cd8c) → `006e6f4d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cd94`](#insn-00c2cd94) → `01128080`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cd98`](#insn-00c2cd98) → [`00c2cdb0`](#insn-00c2cdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cda8`](#insn-00c2cda8) → `01128080`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cdac`](#insn-00c2cdac) → [`00c2cdc4`](#insn-00c2cdc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cdbc`](#insn-00c2cdbc) → `01128090`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cdc0`](#insn-00c2cdc0) → `01128088`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cdcc`](#insn-00c2cdcc) → `01128081`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2cdd4`](#insn-00c2cdd4) → `01128098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cdd8`](#insn-00c2cdd8) → [`00c2cdf0`](#insn-00c2cdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cde8`](#insn-00c2cde8) → `01128098`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cdec`](#insn-00c2cdec) → [`00c2ce04`](#insn-00c2ce04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cdfc`](#insn-00c2cdfc) → `011280a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ce00`](#insn-00c2ce00) → `011280a0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ce0c`](#insn-00c2ce0c) → `01128099`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2ce14`](#insn-00c2ce14) → `011280b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ce18`](#insn-00c2ce18) → [`00c2ce30`](#insn-00c2ce30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ce28`](#insn-00c2ce28) → `011280b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ce2c`](#insn-00c2ce2c) → [`00c2ce44`](#insn-00c2ce44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ce3c`](#insn-00c2ce3c) → `011280c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ce40`](#insn-00c2ce40) → `011280b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ce4c`](#insn-00c2ce4c) → `011280b1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2ce54`](#insn-00c2ce54) → `011280c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ce58`](#insn-00c2ce58) → [`00c2ce70`](#insn-00c2ce70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ce68`](#insn-00c2ce68) → `011280c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ce6c`](#insn-00c2ce6c) → [`00c2ce84`](#insn-00c2ce84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ce7c`](#insn-00c2ce7c) → `011280d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ce80`](#insn-00c2ce80) → `011280d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2ce8c`](#insn-00c2ce8c) → `011280c9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2ce94`](#insn-00c2ce94) → `011280e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ce98`](#insn-00c2ce98) → [`00c2ceb0`](#insn-00c2ceb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cea8`](#insn-00c2cea8) → `011280e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2ceac`](#insn-00c2ceac) → [`00c2cec4`](#insn-00c2cec4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cebc`](#insn-00c2cebc) → `011280f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cec0`](#insn-00c2cec0) → `011280e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2cecc`](#insn-00c2cecc) → `011280e1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2ced0`](#insn-00c2ced0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cee0`](#insn-00c2cee0) → `011280f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cee4`](#insn-00c2cee4) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00c2cee8`](#insn-00c2cee8) → [`00c2caf8`](#insn-00c2caf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2cef0`](#insn-00c2cef0) → [`00c35ba0`](../00c35/00c35ba0.md) · `PARAM` · `ANALYSIS` · 関数 `00c35ba0` · 推定シンボル `None` · 推定型 `None`
- [`00c2cef8`](#insn-00c2cef8) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c2cf00`](#insn-00c2cf00) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00c2cf08`](#insn-00c2cf08) → `011280f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2cf0c`](#insn-00c2cf0c) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00c2cf10`](#insn-00c2cf10) → [`00c2caf8`](#insn-00c2caf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2cae0`](#insn-00c2cae0)

~~~json
{
  "source": "00c2cae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2caf0`](#insn-00c2caf0)

~~~json
{
  "source": "00c2caf0",
  "target": "011280f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2caf4`](#insn-00c2caf4)

~~~json
{
  "source": "00c2caf4",
  "target": "00c2cedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cafc`](#insn-00c2cafc)

~~~json
{
  "source": "00c2cafc",
  "target": "01127fa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fa8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb00`](#insn-00c2cb00)

~~~json
{
  "source": "00c2cb00",
  "target": "00c2cb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb10`](#insn-00c2cb10)

~~~json
{
  "source": "00c2cb10",
  "target": "01127fa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fa8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb14`](#insn-00c2cb14)

~~~json
{
  "source": "00c2cb14",
  "target": "00c2cb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb24`](#insn-00c2cb24)

~~~json
{
  "source": "00c2cb24",
  "target": "01127fb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb28`](#insn-00c2cb28)

~~~json
{
  "source": "00c2cb28",
  "target": "01127fb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb34`](#insn-00c2cb34)

~~~json
{
  "source": "00c2cb34",
  "target": "01127faf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127faf",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb3c`](#insn-00c2cb3c)

~~~json
{
  "source": "00c2cb3c",
  "target": "01127fad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fad",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb44`](#insn-00c2cb44)

~~~json
{
  "source": "00c2cb44",
  "target": "01127fa9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fa9",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb48`](#insn-00c2cb48)

~~~json
{
  "source": "00c2cb48",
  "target": "01127fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb4c`](#insn-00c2cb4c)

~~~json
{
  "source": "00c2cb4c",
  "target": "00c2cb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb5c`](#insn-00c2cb5c)

~~~json
{
  "source": "00c2cb5c",
  "target": "01127fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb60`](#insn-00c2cb60)

~~~json
{
  "source": "00c2cb60",
  "target": "00c2cb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cb70`](#insn-00c2cb70)

~~~json
{
  "source": "00c2cb70",
  "target": "01127fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb74`](#insn-00c2cb74)

~~~json
{
  "source": "00c2cb74",
  "target": "01127fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb80`](#insn-00c2cb80)

~~~json
{
  "source": "00c2cb80",
  "target": "01127fc7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fc7",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb88`](#insn-00c2cb88)

~~~json
{
  "source": "00c2cb88",
  "target": "01127fc5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fc5",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb90`](#insn-00c2cb90)

~~~json
{
  "source": "00c2cb90",
  "target": "01127fc1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fc1",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb94`](#insn-00c2cb94)

~~~json
{
  "source": "00c2cb94",
  "target": "01127fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cb98`](#insn-00c2cb98)

~~~json
{
  "source": "00c2cb98",
  "target": "00c2cbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cba8`](#insn-00c2cba8)

~~~json
{
  "source": "00c2cba8",
  "target": "01127fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbac`](#insn-00c2cbac)

~~~json
{
  "source": "00c2cbac",
  "target": "00c2cbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cbbc`](#insn-00c2cbbc)

~~~json
{
  "source": "00c2cbbc",
  "target": "01127fe8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fe8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbc0`](#insn-00c2cbc0)

~~~json
{
  "source": "00c2cbc0",
  "target": "01127fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fe0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbcc`](#insn-00c2cbcc)

~~~json
{
  "source": "00c2cbcc",
  "target": "01127fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fe0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbd8`](#insn-00c2cbd8)

~~~json
{
  "source": "00c2cbd8",
  "target": "01127fdc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fd9",
  "offset": 3,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbe0`](#insn-00c2cbe0)

~~~json
{
  "source": "00c2cbe0",
  "target": "01127fd9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fd9",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbe4`](#insn-00c2cbe4)

~~~json
{
  "source": "00c2cbe4",
  "target": "01127ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbe8`](#insn-00c2cbe8)

~~~json
{
  "source": "00c2cbe8",
  "target": "00c2cc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cbf8`](#insn-00c2cbf8)

~~~json
{
  "source": "00c2cbf8",
  "target": "01127ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cbfc`](#insn-00c2cbfc)

~~~json
{
  "source": "00c2cbfc",
  "target": "00c2cc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cc0c`](#insn-00c2cc0c)

~~~json
{
  "source": "00c2cc0c",
  "target": "01128000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc10`](#insn-00c2cc10)

~~~json
{
  "source": "00c2cc10",
  "target": "01127ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff1",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc20`](#insn-00c2cc20)

~~~json
{
  "source": "00c2cc20",
  "target": "002b8d72",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8d72",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "5765646e657364617900",
  "capture_start": "002b8d72",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c2cc24`](#insn-00c2cc24)

~~~json
{
  "source": "00c2cc24",
  "target": "01127ff9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff9",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc28`](#insn-00c2cc28)

~~~json
{
  "source": "00c2cc28",
  "target": "01127ff1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ff1",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc30`](#insn-00c2cc30)

~~~json
{
  "source": "00c2cc30",
  "target": "01128008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128008",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc34`](#insn-00c2cc34)

~~~json
{
  "source": "00c2cc34",
  "target": "00c2cc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cc44`](#insn-00c2cc44)

~~~json
{
  "source": "00c2cc44",
  "target": "01128008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128008",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc48`](#insn-00c2cc48)

~~~json
{
  "source": "00c2cc48",
  "target": "00c2cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cc58`](#insn-00c2cc58)

~~~json
{
  "source": "00c2cc58",
  "target": "01128018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc5c`](#insn-00c2cc5c)

~~~json
{
  "source": "00c2cc5c",
  "target": "01128010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128009",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc64`](#insn-00c2cc64)

~~~json
{
  "source": "00c2cc64",
  "target": "01128011",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128011",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc74`](#insn-00c2cc74)

~~~json
{
  "source": "00c2cc74",
  "target": "01128009",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128009",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc7c`](#insn-00c2cc7c)

~~~json
{
  "source": "00c2cc7c",
  "target": "01128020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128020",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc80`](#insn-00c2cc80)

~~~json
{
  "source": "00c2cc80",
  "target": "00c2cc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cc90`](#insn-00c2cc90)

~~~json
{
  "source": "00c2cc90",
  "target": "01128020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128020",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cc94`](#insn-00c2cc94)

~~~json
{
  "source": "00c2cc94",
  "target": "00c2ccac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cca4`](#insn-00c2cca4)

~~~json
{
  "source": "00c2cca4",
  "target": "01128030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cca8`](#insn-00c2cca8)

~~~json
{
  "source": "00c2cca8",
  "target": "01128028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ccb4`](#insn-00c2ccb4)

~~~json
{
  "source": "00c2ccb4",
  "target": "01128027",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128027",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ccbc`](#insn-00c2ccbc)

~~~json
{
  "source": "00c2ccbc",
  "target": "01128025",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128025",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ccc4`](#insn-00c2ccc4)

~~~json
{
  "source": "00c2ccc4",
  "target": "01128021",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128021",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ccc8`](#insn-00c2ccc8)

~~~json
{
  "source": "00c2ccc8",
  "target": "01128038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cccc`](#insn-00c2cccc)

~~~json
{
  "source": "00c2cccc",
  "target": "00c2cce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ccdc`](#insn-00c2ccdc)

~~~json
{
  "source": "00c2ccdc",
  "target": "01128038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cce0`](#insn-00c2cce0)

~~~json
{
  "source": "00c2cce0",
  "target": "00c2ccf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ccf0`](#insn-00c2ccf0)

~~~json
{
  "source": "00c2ccf0",
  "target": "01128048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ccf4`](#insn-00c2ccf4)

~~~json
{
  "source": "00c2ccf4",
  "target": "01128040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128039",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ccfc`](#insn-00c2ccfc)

~~~json
{
  "source": "00c2ccfc",
  "target": "01128041",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128041",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd0c`](#insn-00c2cd0c)

~~~json
{
  "source": "00c2cd0c",
  "target": "01128039",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128039",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd14`](#insn-00c2cd14)

~~~json
{
  "source": "00c2cd14",
  "target": "01128050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128050",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd18`](#insn-00c2cd18)

~~~json
{
  "source": "00c2cd18",
  "target": "00c2cd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cd28`](#insn-00c2cd28)

~~~json
{
  "source": "00c2cd28",
  "target": "01128050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128050",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd2c`](#insn-00c2cd2c)

~~~json
{
  "source": "00c2cd2c",
  "target": "00c2cd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cd3c`](#insn-00c2cd3c)

~~~json
{
  "source": "00c2cd3c",
  "target": "01128060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd40`](#insn-00c2cd40)

~~~json
{
  "source": "00c2cd40",
  "target": "01128058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd4c`](#insn-00c2cd4c)

~~~json
{
  "source": "00c2cd4c",
  "target": "01128051",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128051",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd54`](#insn-00c2cd54)

~~~json
{
  "source": "00c2cd54",
  "target": "01128068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128068",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd58`](#insn-00c2cd58)

~~~json
{
  "source": "00c2cd58",
  "target": "00c2cd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cd68`](#insn-00c2cd68)

~~~json
{
  "source": "00c2cd68",
  "target": "01128068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128068",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd6c`](#insn-00c2cd6c)

~~~json
{
  "source": "00c2cd6c",
  "target": "00c2cd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cd7c`](#insn-00c2cd7c)

~~~json
{
  "source": "00c2cd7c",
  "target": "01128078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128078",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd80`](#insn-00c2cd80)

~~~json
{
  "source": "00c2cd80",
  "target": "01128070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128070",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd8c`](#insn-00c2cd8c)

~~~json
{
  "source": "00c2cd8c",
  "target": "01128069",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128069",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd8c`](#insn-00c2cd8c)

~~~json
{
  "source": "00c2cd8c",
  "target": "006e6f4d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cd94`](#insn-00c2cd94)

~~~json
{
  "source": "00c2cd94",
  "target": "01128080",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128080",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cd98`](#insn-00c2cd98)

~~~json
{
  "source": "00c2cd98",
  "target": "00c2cdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cda8`](#insn-00c2cda8)

~~~json
{
  "source": "00c2cda8",
  "target": "01128080",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128080",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cdac`](#insn-00c2cdac)

~~~json
{
  "source": "00c2cdac",
  "target": "00c2cdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cdbc`](#insn-00c2cdbc)

~~~json
{
  "source": "00c2cdbc",
  "target": "01128090",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128090",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cdc0`](#insn-00c2cdc0)

~~~json
{
  "source": "00c2cdc0",
  "target": "01128088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128088",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cdcc`](#insn-00c2cdcc)

~~~json
{
  "source": "00c2cdcc",
  "target": "01128081",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128081",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cdd4`](#insn-00c2cdd4)

~~~json
{
  "source": "00c2cdd4",
  "target": "01128098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128098",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cdd8`](#insn-00c2cdd8)

~~~json
{
  "source": "00c2cdd8",
  "target": "00c2cdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cde8`](#insn-00c2cde8)

~~~json
{
  "source": "00c2cde8",
  "target": "01128098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128098",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cdec`](#insn-00c2cdec)

~~~json
{
  "source": "00c2cdec",
  "target": "00c2ce04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cdfc`](#insn-00c2cdfc)

~~~json
{
  "source": "00c2cdfc",
  "target": "011280a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce00`](#insn-00c2ce00)

~~~json
{
  "source": "00c2ce00",
  "target": "011280a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce0c`](#insn-00c2ce0c)

~~~json
{
  "source": "00c2ce0c",
  "target": "01128099",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128099",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce14`](#insn-00c2ce14)

~~~json
{
  "source": "00c2ce14",
  "target": "011280b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce18`](#insn-00c2ce18)

~~~json
{
  "source": "00c2ce18",
  "target": "00c2ce30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ce28`](#insn-00c2ce28)

~~~json
{
  "source": "00c2ce28",
  "target": "011280b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce2c`](#insn-00c2ce2c)

~~~json
{
  "source": "00c2ce2c",
  "target": "00c2ce44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ce3c`](#insn-00c2ce3c)

~~~json
{
  "source": "00c2ce3c",
  "target": "011280c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce40`](#insn-00c2ce40)

~~~json
{
  "source": "00c2ce40",
  "target": "011280b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce4c`](#insn-00c2ce4c)

~~~json
{
  "source": "00c2ce4c",
  "target": "011280b1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280b1",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce54`](#insn-00c2ce54)

~~~json
{
  "source": "00c2ce54",
  "target": "011280c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280c8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce58`](#insn-00c2ce58)

~~~json
{
  "source": "00c2ce58",
  "target": "00c2ce70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ce68`](#insn-00c2ce68)

~~~json
{
  "source": "00c2ce68",
  "target": "011280c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280c8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce6c`](#insn-00c2ce6c)

~~~json
{
  "source": "00c2ce6c",
  "target": "00c2ce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ce7c`](#insn-00c2ce7c)

~~~json
{
  "source": "00c2ce7c",
  "target": "011280d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce80`](#insn-00c2ce80)

~~~json
{
  "source": "00c2ce80",
  "target": "011280d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce8c`](#insn-00c2ce8c)

~~~json
{
  "source": "00c2ce8c",
  "target": "011280c9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280c9",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce94`](#insn-00c2ce94)

~~~json
{
  "source": "00c2ce94",
  "target": "011280e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ce98`](#insn-00c2ce98)

~~~json
{
  "source": "00c2ce98",
  "target": "00c2ceb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cea8`](#insn-00c2cea8)

~~~json
{
  "source": "00c2cea8",
  "target": "011280e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ceac`](#insn-00c2ceac)

~~~json
{
  "source": "00c2ceac",
  "target": "00c2cec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cebc`](#insn-00c2cebc)

~~~json
{
  "source": "00c2cebc",
  "target": "011280f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cec0`](#insn-00c2cec0)

~~~json
{
  "source": "00c2cec0",
  "target": "011280e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cecc`](#insn-00c2cecc)

~~~json
{
  "source": "00c2cecc",
  "target": "011280e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280e1",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2ced0`](#insn-00c2ced0)

~~~json
{
  "source": "00c2ced0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cee0`](#insn-00c2cee0)

~~~json
{
  "source": "00c2cee0",
  "target": "011280f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cee4`](#insn-00c2cee4)

~~~json
{
  "source": "00c2cee4",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cee8`](#insn-00c2cee8)

~~~json
{
  "source": "00c2cee8",
  "target": "00c2caf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2cef0`](#insn-00c2cef0)

~~~json
{
  "source": "00c2cef0",
  "target": "00c35ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cef8`](#insn-00c2cef8)

~~~json
{
  "source": "00c2cef8",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c2cf00`](#insn-00c2cf00)

~~~json
{
  "source": "00c2cf00",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cf08`](#insn-00c2cf08)

~~~json
{
  "source": "00c2cf08",
  "target": "011280f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011280f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2cf0c`](#insn-00c2cf0c)

~~~json
{
  "source": "00c2cf0c",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2cf10`](#insn-00c2cf10)

~~~json
{
  "source": "00c2cf10",
  "target": "00c2caf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
