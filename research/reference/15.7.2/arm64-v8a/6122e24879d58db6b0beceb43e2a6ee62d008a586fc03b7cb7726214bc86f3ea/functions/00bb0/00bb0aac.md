# 00bb0aac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/review-0021.md#review-e48f5a3758dd035a7cb9aa85075abb31)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb0aac",
  "name": "FUN_00bb0aac",
  "size": 1320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "497bcf393198010e09d2386e052e8436a266ae1d87ea8488fbcd1f6acac72ac3",
  "source_text_sha256": "497bcf393198010e09d2386e052e8436a266ae1d87ea8488fbcd1f6acac72ac3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb0aac",
        "00bb0fd3"
      ]
    ],
    "bytes_sha256": "e898951a247d457e4e16b4fd6d65ecc954e8a962913da95dea94816790379a48",
    "instruction_count": 330,
    "instruction_bytes": 1320,
    "body_bytes": 1320,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bb0a2c](../00bb0/00bb0a2c.md)

## 呼び出し先

- [00b76424](../00b76/00b76424.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)

## 関連文字列（未確認候補）

~~~text
"April"
"August"
"December"
"February"
"January"
"March"
"November"
"October"
"September"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6290 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00bb0aac(void)

{
  undefined8 uVar1;
  int iVar2;
  undefined8 *puVar3;
  
  if (((DAT_010a32d8 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_010a32d8), iVar2 != 0)) {
    __cxa_atexit(FUN_00bb8f54,0,&PTR_LOOP_00be5ed0);
    __cxa_guard_release(&DAT_010a32d8);
  }
  FUN_00b76424(&DAT_010a3098,L"January",7);
  FUN_00b76424(&DAT_010a30b0,L"February",8);
  FUN_00b76424(&DAT_010a30c8,L"March",5);
  FUN_00b76424(&DAT_010a30e0,L"April",5);
  if ((DAT_010a30f8 & 1) == 0) {
    DAT_010a30f8 = 6;
    puVar3 = &DAT_010a30fc;
  }
  else {
    ram0x010a3100 = 3;
    puVar3 = ram0x010a3108;
  }
  *puVar3 = 0x610000004d;
  puVar3[1] = 0x79;
  if ((DAT_010a3110 & 1) == 0) {
    DAT_010a3110 = 8;
    puVar3 = (undefined8 *)&DAT_010a3114;
  }
  else {
    DAT_010a3118 = 4;
    puVar3 = DAT_010a3120;
  }
                    /* try { // try from 00bb0b9c to 00cb0ba3 has its CatchHandler @ 00bb0ce0 */
  *(undefined4 *)(puVar3 + 2) = 0;
  uVar1 = _DAT_002fa96c;
  puVar3[1] = _UNK_002fa974;
  *puVar3 = uVar1;
  uVar1 = _DAT_002fa6b8;
  if ((DAT_010a3128 & 1) == 0) {
    DAT_010a3128 = 8;
    puVar3 = (undefined8 *)&DAT_010a312c;
  }
  else {
    DAT_010a3130 = 4;
    puVar3 = DAT_010a3138;
  }
  puVar3[1] = _UNK_002fa6c0;
  *puVar3 = uVar1;
  *(undefined4 *)(puVar3 + 2) = 0;
  FUN_00b76424(&DAT_010a3140,L"August",6);
  FUN_00b76424(&DAT_010a3158,L"September",9);
  FUN_00b76424(&DAT_010a3170,L"October",7);
  FUN_00b76424(&DAT_010a3188,L"November",8);
  FUN_00b76424(&DAT_010a31a0,L"December",8);
                    /* try { // try from 00bb0c68 to 00cb0c87 has its CatchHandler @ 00bb0d18 */
  if ((DAT_010a31b8 & 1) == 0) {
    DAT_010a31b8 = 6;
    puVar3 = &DAT_010a31bc;
  }
  else {
    ram0x010a31c0 = 3;
    puVar3 = ram0x010a31c8;
  }
                    /* try { // try from 00bb0c9c to 00cb0ca7 has its CatchHandler @ 00bb0cfc */
  *puVar3 = 0x610000004a;
  puVar3[1] = 0x6e;
  if ((DAT_010a31d0 & 1) == 0) {
    DAT_010a31d0 = 6;
    puVar3 = &DAT_010a31d4;
                    /* try { // try from 00bb0cbc to 00cb0cdb has its CatchHandler @ 00bb0ce4 */
  }
  else {
    ram0x010a31d8 = 3;
    puVar3 = ram0x010a31e0;
  }
                    /* catch() { ... } // from try @ 00bb019c with catch @ 00bb0cdc
                       try { // try from 00bb0cdc to 00cb0d6f has its CatchHandler @ 00bafa54 */
                    /* catch() { ... } // from try @ 00bb0b9c with catch @ 00bb0ce0 */
  *puVar3 = 0x6500000046;
  puVar3[1] = 0x62;
                    /* catch() { ... } // from try @ 00bb0cbc with catch @ 00bb0ce4 */
                    /* catch() { ... } // from try @ 00baff74 with catch @ 00bb0ce8 */
                    /* catch() { ... } // from try @ 00bb09ec with catch @ 00bb0cec */
  if ((DAT_010a31e8 & 1) == 0) {
                    /* catch() { ... } // from try @ 00bb0a54 with catch @ 00bb0cf0 */
                    /* catch() { ... } // from try @ 00bafc78 with catch @ 00bb0cf4 */
                    /* catch() { ... } // from try @ 00bb059c with catch @ 00bb0cf8 */
                    /* catch() { ... } // from try @ 00bb0c9c with catch @ 00bb0cfc */
    DAT_010a31e8 = 6;
    puVar3 = &DAT_010a31ec;
                    /* catch() { ... } // from try @ 00bafb5c with catch @ 00bb0d00 */
  }
  else {
                    /* catch() { ... } // from try @ 00bb0698 with catch @ 00bb0d08 */
                    /* catch() { ... } // from try @ 00bafaac with catch @ 00bb0d0c */
                    /* catch() { ... } // from try @ 00bb0290 with catch @ 00bb0d14 */
    ram0x010a31f0 = 3;
    puVar3 = ram0x010a31f8;
  }
                    /* catch() { ... } // from try @ 00bb0c68 with catch @ 00bb0d18 */
                    /* catch() { ... } // from try @ 00bb000c with catch @ 00bb0d1c */
                    /* catch() { ... } // from try @ 00bb0270 with catch @ 00bb0d20 */
                    /* catch() { ... } // from try @ 00bb06a8 with catch @ 00bb0d24 */
  *puVar3 = 0x610000004d;
  puVar3[1] = 0x72;
                    /* catch() { ... } // from try @ 00bb02a0 with catch @ 00bb0d28 */
                    /* catch() { ... } // from try @ 00bafd44 with catch @ 00bb0d2c */
  if ((DAT_010a3200 & 1) == 0) {
    DAT_010a3200 = 6;
    puVar3 = &DAT_010a3204;
  }
  else {
    ram0x010a3208 = 3;
    puVar3 = ram0x010a3210;
  }
  *puVar3 = 0x7000000041;
  puVar3[1] = 0x72;
  if ((DAT_010a3218 & 1) == 0) {
    DAT_010a3218 = 6;
    puVar3 = &DAT_010a321c;
  }
  else {
                    /* catch() { ... } // from try @ 00bb0f74 with catch @ 00bb0d98 */
    ram0x010a3220 = 3;
    puVar3 = ram0x010a3228;
  }
  *puVar3 = 0x610000004d;
  puVar3[1] = 0x79;
  if ((DAT_010a3230 & 1) == 0) {
    DAT_010a3230 = 6;
    puVar3 = &DAT_010a3234;
  }
  else {
    ram0x010a3238 = 3;
    puVar3 = ram0x010a3240;
  }
  *puVar3 = 0x750000004a;
  puVar3[1] = 0x6e;
  if ((DAT_010a3248 & 1) == 0) {
    DAT_010a3248 = 6;
    puVar3 = &DAT_010a324c;
  }
  else {
    ram0x010a3250 = 3;
    puVar3 = ram0x010a3258;
  }
  *puVar3 = 0x750000004a;
  puVar3[1] = 0x6c;
  if ((DAT_010a3260 & 1) == 0) {
    DAT_010a3260 = 6;
    puVar3 = &DAT_010a3264;
  }
  else {
    ram0x010a3268 = 3;
    puVar3 = ram0x010a3270;
  }
  *puVar3 = 0x7500000041;
  puVar3[1] = 0x67;
  if ((DAT_010a3278 & 1) == 0) {
    DAT_010a3278 = 6;
    puVar3 = &DAT_010a327c;
  }
  else {
    ram0x010a3280 = 3;
    puVar3 = ram0x010a3288;
  }
  *puVar3 = 0x6500000053;
  puVar3[1] = 0x70;
  if ((DAT_010a3290 & 1) == 0) {
    DAT_010a3290 = 6;
    puVar3 = &DAT_010a3294;
  }
  else {
                    /* try { // try from 00bb0eec to 00cb0f73 has its CatchHandler @ 00bb1058 */
    ram0x010a3298 = 3;
    puVar3 = ram0x010a32a0;
  }
  *puVar3 = 0x630000004f;
  puVar3[1] = 0x74;
  if ((DAT_010a32a8 & 1) == 0) {
    DAT_010a32a8 = 6;
    puVar3 = &DAT_010a32ac;
  }
  else {
    ram0x010a32b0 = 3;
    puVar3 = ram0x010a32b8;
  }
  *puVar3 = 0x6f0000004e;
  puVar3[1] = 0x76;
  if ((DAT_010a32c0 & 1) == 0) {
    DAT_010a32c0 = 6;
    puVar3 = &DAT_010a32c4;
  }
  else {
                    /* try { // try from 00bb0f74 to 00cb1127 has its CatchHandler @ 00bb0d98 */
    ram0x010a32c8 = 3;
    puVar3 = ram0x010a32d0;
  }
  *puVar3 = 0x6500000044;
  puVar3[1] = 99;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb0aac"></a> `00bb0aac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb0ab0"></a> `00bb0ab0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb0ab4"></a> `00bb0ab4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0ab8"></a> `00bb0ab8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bb0abc"></a> `00bb0abc` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ac0"></a> `00bb0ac0` | `08 61 0b 91` | add x8,x8,#0x2d8 | `FALL_THROUGH`
<a id="insn-00bb0ac4"></a> `00bb0ac4` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bb0ac8"></a> `00bb0ac8` | `a8 26 00 36` | tbz w8,#0x0,0x00bb0f9c | `CONDITIONAL_JUMP`
<a id="insn-00bb0acc"></a> `00bb0acc` | `93 27 00 f0` | adrp x19,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ad0"></a> `00bb0ad0` | `73 62 02 91` | add x19,x19,#0x98 | `FALL_THROUGH`
<a id="insn-00bb0ad4"></a> `00bb0ad4` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0ad8"></a> `00bb0ad8` | `21 30 1b 91` | add x1,x1,#0x6cc | `FALL_THROUGH`
<a id="insn-00bb0adc"></a> `00bb0adc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb0ae0"></a> `00bb0ae0` | `e2 00 80 52` | mov w2,#0x7 | `FALL_THROUGH`
<a id="insn-00bb0ae4"></a> `00bb0ae4` | `50 16 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0ae8"></a> `00bb0ae8` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0aec"></a> `00bb0aec` | `21 f0 21 91` | add x1,x1,#0x87c | `FALL_THROUGH`
<a id="insn-00bb0af0"></a> `00bb0af0` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bb0af4"></a> `00bb0af4` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0af8"></a> `00bb0af8` | `4b 16 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0afc"></a> `00bb0afc` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0b00"></a> `00bb0b00` | `21 50 25 91` | add x1,x1,#0x954 | `FALL_THROUGH`
<a id="insn-00bb0b04"></a> `00bb0b04` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bb0b08"></a> `00bb0b08` | `a2 00 80 52` | mov w2,#0x5 | `FALL_THROUGH`
<a id="insn-00bb0b0c"></a> `00bb0b0c` | `46 16 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0b10"></a> `00bb0b10` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0b14"></a> `00bb0b14` | `21 20 1d 91` | add x1,x1,#0x748 | `FALL_THROUGH`
<a id="insn-00bb0b18"></a> `00bb0b18` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00bb0b1c"></a> `00bb0b1c` | `a2 00 80 52` | mov w2,#0x5 | `FALL_THROUGH`
<a id="insn-00bb0b20"></a> `00bb0b20` | `41 16 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0b24"></a> `00bb0b24` | `68 82 41 39` | ldrb w8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bb0b28"></a> `00bb0b28` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0b40 | `CONDITIONAL_JUMP`
<a id="insn-00bb0b2c"></a> `00bb0b2c` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0b30"></a> `00bb0b30` | `08 e1 03 91` | add x8,x8,#0xf8 | `FALL_THROUGH`
<a id="insn-00bb0b34"></a> `00bb0b34` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0b38"></a> `00bb0b38` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0b3c"></a> `00bb0b3c` | `06 00 00 14` | b 0x00bb0b54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0b40"></a> `00bb0b40` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0b44"></a> `00bb0b44` | `29 01 04 91` | add x9,x9,#0x100 | `FALL_THROUGH`
<a id="insn-00bb0b48"></a> `00bb0b48` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0b4c"></a> `00bb0b4c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0b50"></a> `00bb0b50` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0b54"></a> `00bb0b54` | `a9 09 80 d2` | mov x9,#0x4d | `FALL_THROUGH`
<a id="insn-00bb0b58"></a> `00bb0b58` | `2a 0f 80 52` | mov w10,#0x79 | `FALL_THROUGH`
<a id="insn-00bb0b5c"></a> `00bb0b5c` | `29 0c c0 f2` | movk x9,#0x61, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0b60"></a> `00bb0b60` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0b64"></a> `00bb0b64` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0b68"></a> `00bb0b68` | `08 41 44 39` | ldrb w8,[x8, #0x110] | `FALL_THROUGH`
<a id="insn-00bb0b6c"></a> `00bb0b6c` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0b84 | `CONDITIONAL_JUMP`
<a id="insn-00bb0b70"></a> `00bb0b70` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0b74"></a> `00bb0b74` | `08 41 04 91` | add x8,x8,#0x110 | `FALL_THROUGH`
<a id="insn-00bb0b78"></a> `00bb0b78` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0b7c"></a> `00bb0b7c` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0b80"></a> `00bb0b80` | `06 00 00 14` | b 0x00bb0b98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0b84"></a> `00bb0b84` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0b88"></a> `00bb0b88` | `29 61 04 91` | add x9,x9,#0x118 | `FALL_THROUGH`
<a id="insn-00bb0b8c"></a> `00bb0b8c` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00bb0b90"></a> `00bb0b90` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0b94"></a> `00bb0b94` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0b98"></a> `00bb0b98` | `49 ba ff d0` | adrp x9,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0b9c"></a> `00bb0b9c` | `29 b1 25 91` | add x9,x9,#0x96c | `FALL_THROUGH`
<a id="insn-00bb0ba0"></a> `00bb0ba0` | `1f 11 00 b9` | str wzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0ba4"></a> `00bb0ba4` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00bb0ba8"></a> `00bb0ba8` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bb0bac"></a> `00bb0bac` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0bb0"></a> `00bb0bb0` | `08 a1 44 39` | ldrb w8,[x8, #0x128] | `FALL_THROUGH`
<a id="insn-00bb0bb4"></a> `00bb0bb4` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0bcc | `CONDITIONAL_JUMP`
<a id="insn-00bb0bb8"></a> `00bb0bb8` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0bbc"></a> `00bb0bbc` | `08 a1 04 91` | add x8,x8,#0x128 | `FALL_THROUGH`
<a id="insn-00bb0bc0"></a> `00bb0bc0` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0bc4"></a> `00bb0bc4` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0bc8"></a> `00bb0bc8` | `06 00 00 14` | b 0x00bb0be0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0bcc"></a> `00bb0bcc` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0bd0"></a> `00bb0bd0` | `29 c1 04 91` | add x9,x9,#0x130 | `FALL_THROUGH`
<a id="insn-00bb0bd4"></a> `00bb0bd4` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00bb0bd8"></a> `00bb0bd8` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0bdc"></a> `00bb0bdc` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0be0"></a> `00bb0be0` | `49 ba ff d0` | adrp x9,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0be4"></a> `00bb0be4` | `29 e1 1a 91` | add x9,x9,#0x6b8 | `FALL_THROUGH`
<a id="insn-00bb0be8"></a> `00bb0be8` | `93 27 00 f0` | adrp x19,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0bec"></a> `00bb0bec` | `73 02 05 91` | add x19,x19,#0x140 | `FALL_THROUGH`
<a id="insn-00bb0bf0"></a> `00bb0bf0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00bb0bf4"></a> `00bb0bf4` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0bf8"></a> `00bb0bf8` | `21 80 19 91` | add x1,x1,#0x660 | `FALL_THROUGH`
<a id="insn-00bb0bfc"></a> `00bb0bfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb0c00"></a> `00bb0c00` | `c2 00 80 52` | mov w2,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0c04"></a> `00bb0c04` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bb0c08"></a> `00bb0c08` | `d4 00 80 52` | mov w20,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0c0c"></a> `00bb0c0c` | `1f 11 00 b9` | str wzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0c10"></a> `00bb0c10` | `05 16 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0c14"></a> `00bb0c14` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0c18"></a> `00bb0c18` | `21 f0 1b 91` | add x1,x1,#0x6fc | `FALL_THROUGH`
<a id="insn-00bb0c1c"></a> `00bb0c1c` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bb0c20"></a> `00bb0c20` | `22 01 80 52` | mov w2,#0x9 | `FALL_THROUGH`
<a id="insn-00bb0c24"></a> `00bb0c24` | `00 16 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0c28"></a> `00bb0c28` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0c2c"></a> `00bb0c2c` | `21 80 22 91` | add x1,x1,#0x8a0 | `FALL_THROUGH`
<a id="insn-00bb0c30"></a> `00bb0c30` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bb0c34"></a> `00bb0c34` | `e2 00 80 52` | mov w2,#0x7 | `FALL_THROUGH`
<a id="insn-00bb0c38"></a> `00bb0c38` | `fb 15 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0c3c"></a> `00bb0c3c` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0c40"></a> `00bb0c40` | `21 80 1e 91` | add x1,x1,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bb0c44"></a> `00bb0c44` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00bb0c48"></a> `00bb0c48` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0c4c"></a> `00bb0c4c` | `f6 15 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0c50"></a> `00bb0c50` | `41 ba ff d0` | adrp x1,0x2fa000 | `FALL_THROUGH`
<a id="insn-00bb0c54"></a> `00bb0c54` | `21 90 1c 91` | add x1,x1,#0x724 | `FALL_THROUGH`
<a id="insn-00bb0c58"></a> `00bb0c58` | `60 82 01 91` | add x0,x19,#0x60 | `FALL_THROUGH`
<a id="insn-00bb0c5c"></a> `00bb0c5c` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0c60"></a> `00bb0c60` | `f1 15 ff 97` | bl 0x00b76424 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0c64"></a> `00bb0c64` | `68 e2 41 39` | ldrb w8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bb0c68"></a> `00bb0c68` | `a8 00 00 37` | tbnz w8,#0x0,0x00bb0c7c | `CONDITIONAL_JUMP`
<a id="insn-00bb0c6c"></a> `00bb0c6c` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0c70"></a> `00bb0c70` | `08 e1 06 91` | add x8,x8,#0x1b8 | `FALL_THROUGH`
<a id="insn-00bb0c74"></a> `00bb0c74` | `14 45 00 38` | strb w20,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0c78"></a> `00bb0c78` | `06 00 00 14` | b 0x00bb0c90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0c7c"></a> `00bb0c7c` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0c80"></a> `00bb0c80` | `29 01 07 91` | add x9,x9,#0x1c0 | `FALL_THROUGH`
<a id="insn-00bb0c84"></a> `00bb0c84` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0c88"></a> `00bb0c88` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0c8c"></a> `00bb0c8c` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0c90"></a> `00bb0c90` | `49 09 80 d2` | mov x9,#0x4a | `FALL_THROUGH`
<a id="insn-00bb0c94"></a> `00bb0c94` | `ca 0d 80 52` | mov w10,#0x6e | `FALL_THROUGH`
<a id="insn-00bb0c98"></a> `00bb0c98` | `29 0c c0 f2` | movk x9,#0x61, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0c9c"></a> `00bb0c9c` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0ca0"></a> `00bb0ca0` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ca4"></a> `00bb0ca4` | `08 41 47 39` | ldrb w8,[x8, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bb0ca8"></a> `00bb0ca8` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0cc0 | `CONDITIONAL_JUMP`
<a id="insn-00bb0cac"></a> `00bb0cac` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0cb0"></a> `00bb0cb0` | `08 41 07 91` | add x8,x8,#0x1d0 | `FALL_THROUGH`
<a id="insn-00bb0cb4"></a> `00bb0cb4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0cb8"></a> `00bb0cb8` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0cbc"></a> `00bb0cbc` | `06 00 00 14` | b 0x00bb0cd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0cc0"></a> `00bb0cc0` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0cc4"></a> `00bb0cc4` | `29 61 07 91` | add x9,x9,#0x1d8 | `FALL_THROUGH`
<a id="insn-00bb0cc8"></a> `00bb0cc8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0ccc"></a> `00bb0ccc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0cd0"></a> `00bb0cd0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0cd4"></a> `00bb0cd4` | `c9 08 80 d2` | mov x9,#0x46 | `FALL_THROUGH`
<a id="insn-00bb0cd8"></a> `00bb0cd8` | `4a 0c 80 52` | mov w10,#0x62 | `FALL_THROUGH`
<a id="insn-00bb0cdc"></a> `00bb0cdc` | `a9 0c c0 f2` | movk x9,#0x65, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0ce0"></a> `00bb0ce0` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0ce4"></a> `00bb0ce4` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ce8"></a> `00bb0ce8` | `08 a1 47 39` | ldrb w8,[x8, #0x1e8] | `FALL_THROUGH`
<a id="insn-00bb0cec"></a> `00bb0cec` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0d04 | `CONDITIONAL_JUMP`
<a id="insn-00bb0cf0"></a> `00bb0cf0` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0cf4"></a> `00bb0cf4` | `08 a1 07 91` | add x8,x8,#0x1e8 | `FALL_THROUGH`
<a id="insn-00bb0cf8"></a> `00bb0cf8` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0cfc"></a> `00bb0cfc` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0d00"></a> `00bb0d00` | `06 00 00 14` | b 0x00bb0d18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0d04"></a> `00bb0d04` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d08"></a> `00bb0d08` | `29 c1 07 91` | add x9,x9,#0x1f0 | `FALL_THROUGH`
<a id="insn-00bb0d0c"></a> `00bb0d0c` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0d10"></a> `00bb0d10` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0d14"></a> `00bb0d14` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0d18"></a> `00bb0d18` | `a9 09 80 d2` | mov x9,#0x4d | `FALL_THROUGH`
<a id="insn-00bb0d1c"></a> `00bb0d1c` | `4a 0e 80 52` | mov w10,#0x72 | `FALL_THROUGH`
<a id="insn-00bb0d20"></a> `00bb0d20` | `29 0c c0 f2` | movk x9,#0x61, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0d24"></a> `00bb0d24` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0d28"></a> `00bb0d28` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d2c"></a> `00bb0d2c` | `08 01 48 39` | ldrb w8,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bb0d30"></a> `00bb0d30` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0d48 | `CONDITIONAL_JUMP`
<a id="insn-00bb0d34"></a> `00bb0d34` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d38"></a> `00bb0d38` | `08 01 08 91` | add x8,x8,#0x200 | `FALL_THROUGH`
<a id="insn-00bb0d3c"></a> `00bb0d3c` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0d40"></a> `00bb0d40` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0d44"></a> `00bb0d44` | `06 00 00 14` | b 0x00bb0d5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0d48"></a> `00bb0d48` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d4c"></a> `00bb0d4c` | `29 21 08 91` | add x9,x9,#0x208 | `FALL_THROUGH`
<a id="insn-00bb0d50"></a> `00bb0d50` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0d54"></a> `00bb0d54` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0d58"></a> `00bb0d58` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0d5c"></a> `00bb0d5c` | `29 08 80 d2` | mov x9,#0x41 | `FALL_THROUGH`
<a id="insn-00bb0d60"></a> `00bb0d60` | `4a 0e 80 52` | mov w10,#0x72 | `FALL_THROUGH`
<a id="insn-00bb0d64"></a> `00bb0d64` | `09 0e c0 f2` | movk x9,#0x70, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0d68"></a> `00bb0d68` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0d6c"></a> `00bb0d6c` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d70"></a> `00bb0d70` | `08 61 48 39` | ldrb w8,[x8, #0x218] | `FALL_THROUGH`
<a id="insn-00bb0d74"></a> `00bb0d74` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0d8c | `CONDITIONAL_JUMP`
<a id="insn-00bb0d78"></a> `00bb0d78` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d7c"></a> `00bb0d7c` | `08 61 08 91` | add x8,x8,#0x218 | `FALL_THROUGH`
<a id="insn-00bb0d80"></a> `00bb0d80` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0d84"></a> `00bb0d84` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0d88"></a> `00bb0d88` | `06 00 00 14` | b 0x00bb0da0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0d8c"></a> `00bb0d8c` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0d90"></a> `00bb0d90` | `29 81 08 91` | add x9,x9,#0x220 | `FALL_THROUGH`
<a id="insn-00bb0d94"></a> `00bb0d94` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0d98"></a> `00bb0d98` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0d9c"></a> `00bb0d9c` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0da0"></a> `00bb0da0` | `a9 09 80 d2` | mov x9,#0x4d | `FALL_THROUGH`
<a id="insn-00bb0da4"></a> `00bb0da4` | `2a 0f 80 52` | mov w10,#0x79 | `FALL_THROUGH`
<a id="insn-00bb0da8"></a> `00bb0da8` | `29 0c c0 f2` | movk x9,#0x61, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0dac"></a> `00bb0dac` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0db0"></a> `00bb0db0` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0db4"></a> `00bb0db4` | `08 c1 48 39` | ldrb w8,[x8, #0x230] | `FALL_THROUGH`
<a id="insn-00bb0db8"></a> `00bb0db8` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0dd0 | `CONDITIONAL_JUMP`
<a id="insn-00bb0dbc"></a> `00bb0dbc` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0dc0"></a> `00bb0dc0` | `08 c1 08 91` | add x8,x8,#0x230 | `FALL_THROUGH`
<a id="insn-00bb0dc4"></a> `00bb0dc4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0dc8"></a> `00bb0dc8` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0dcc"></a> `00bb0dcc` | `06 00 00 14` | b 0x00bb0de4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0dd0"></a> `00bb0dd0` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0dd4"></a> `00bb0dd4` | `29 e1 08 91` | add x9,x9,#0x238 | `FALL_THROUGH`
<a id="insn-00bb0dd8"></a> `00bb0dd8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0ddc"></a> `00bb0ddc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0de0"></a> `00bb0de0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0de4"></a> `00bb0de4` | `49 09 80 d2` | mov x9,#0x4a | `FALL_THROUGH`
<a id="insn-00bb0de8"></a> `00bb0de8` | `ca 0d 80 52` | mov w10,#0x6e | `FALL_THROUGH`
<a id="insn-00bb0dec"></a> `00bb0dec` | `a9 0e c0 f2` | movk x9,#0x75, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0df0"></a> `00bb0df0` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0df4"></a> `00bb0df4` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0df8"></a> `00bb0df8` | `08 21 49 39` | ldrb w8,[x8, #0x248] | `FALL_THROUGH`
<a id="insn-00bb0dfc"></a> `00bb0dfc` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0e14 | `CONDITIONAL_JUMP`
<a id="insn-00bb0e00"></a> `00bb0e00` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e04"></a> `00bb0e04` | `08 21 09 91` | add x8,x8,#0x248 | `FALL_THROUGH`
<a id="insn-00bb0e08"></a> `00bb0e08` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0e0c"></a> `00bb0e0c` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0e10"></a> `00bb0e10` | `06 00 00 14` | b 0x00bb0e28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0e14"></a> `00bb0e14` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e18"></a> `00bb0e18` | `29 41 09 91` | add x9,x9,#0x250 | `FALL_THROUGH`
<a id="insn-00bb0e1c"></a> `00bb0e1c` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0e20"></a> `00bb0e20` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0e24"></a> `00bb0e24` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0e28"></a> `00bb0e28` | `49 09 80 d2` | mov x9,#0x4a | `FALL_THROUGH`
<a id="insn-00bb0e2c"></a> `00bb0e2c` | `8a 0d 80 52` | mov w10,#0x6c | `FALL_THROUGH`
<a id="insn-00bb0e30"></a> `00bb0e30` | `a9 0e c0 f2` | movk x9,#0x75, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0e34"></a> `00bb0e34` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0e38"></a> `00bb0e38` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e3c"></a> `00bb0e3c` | `08 81 49 39` | ldrb w8,[x8, #0x260] | `FALL_THROUGH`
<a id="insn-00bb0e40"></a> `00bb0e40` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0e58 | `CONDITIONAL_JUMP`
<a id="insn-00bb0e44"></a> `00bb0e44` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e48"></a> `00bb0e48` | `08 81 09 91` | add x8,x8,#0x260 | `FALL_THROUGH`
<a id="insn-00bb0e4c"></a> `00bb0e4c` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0e50"></a> `00bb0e50` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0e54"></a> `00bb0e54` | `06 00 00 14` | b 0x00bb0e6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0e58"></a> `00bb0e58` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e5c"></a> `00bb0e5c` | `29 a1 09 91` | add x9,x9,#0x268 | `FALL_THROUGH`
<a id="insn-00bb0e60"></a> `00bb0e60` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0e64"></a> `00bb0e64` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0e68"></a> `00bb0e68` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0e6c"></a> `00bb0e6c` | `29 08 80 d2` | mov x9,#0x41 | `FALL_THROUGH`
<a id="insn-00bb0e70"></a> `00bb0e70` | `ea 0c 80 52` | mov w10,#0x67 | `FALL_THROUGH`
<a id="insn-00bb0e74"></a> `00bb0e74` | `a9 0e c0 f2` | movk x9,#0x75, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0e78"></a> `00bb0e78` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0e7c"></a> `00bb0e7c` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e80"></a> `00bb0e80` | `08 e1 49 39` | ldrb w8,[x8, #0x278] | `FALL_THROUGH`
<a id="insn-00bb0e84"></a> `00bb0e84` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0e9c | `CONDITIONAL_JUMP`
<a id="insn-00bb0e88"></a> `00bb0e88` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0e8c"></a> `00bb0e8c` | `08 e1 09 91` | add x8,x8,#0x278 | `FALL_THROUGH`
<a id="insn-00bb0e90"></a> `00bb0e90` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0e94"></a> `00bb0e94` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0e98"></a> `00bb0e98` | `06 00 00 14` | b 0x00bb0eb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0e9c"></a> `00bb0e9c` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ea0"></a> `00bb0ea0` | `29 01 0a 91` | add x9,x9,#0x280 | `FALL_THROUGH`
<a id="insn-00bb0ea4"></a> `00bb0ea4` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0ea8"></a> `00bb0ea8` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0eac"></a> `00bb0eac` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0eb0"></a> `00bb0eb0` | `69 0a 80 d2` | mov x9,#0x53 | `FALL_THROUGH`
<a id="insn-00bb0eb4"></a> `00bb0eb4` | `0a 0e 80 52` | mov w10,#0x70 | `FALL_THROUGH`
<a id="insn-00bb0eb8"></a> `00bb0eb8` | `a9 0c c0 f2` | movk x9,#0x65, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0ebc"></a> `00bb0ebc` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0ec0"></a> `00bb0ec0` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ec4"></a> `00bb0ec4` | `08 41 4a 39` | ldrb w8,[x8, #0x290] | `FALL_THROUGH`
<a id="insn-00bb0ec8"></a> `00bb0ec8` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0ee0 | `CONDITIONAL_JUMP`
<a id="insn-00bb0ecc"></a> `00bb0ecc` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ed0"></a> `00bb0ed0` | `08 41 0a 91` | add x8,x8,#0x290 | `FALL_THROUGH`
<a id="insn-00bb0ed4"></a> `00bb0ed4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0ed8"></a> `00bb0ed8` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0edc"></a> `00bb0edc` | `06 00 00 14` | b 0x00bb0ef4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0ee0"></a> `00bb0ee0` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0ee4"></a> `00bb0ee4` | `29 61 0a 91` | add x9,x9,#0x298 | `FALL_THROUGH`
<a id="insn-00bb0ee8"></a> `00bb0ee8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0eec"></a> `00bb0eec` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0ef0"></a> `00bb0ef0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0ef4"></a> `00bb0ef4` | `e9 09 80 d2` | mov x9,#0x4f | `FALL_THROUGH`
<a id="insn-00bb0ef8"></a> `00bb0ef8` | `8a 0e 80 52` | mov w10,#0x74 | `FALL_THROUGH`
<a id="insn-00bb0efc"></a> `00bb0efc` | `69 0c c0 f2` | movk x9,#0x63, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0f00"></a> `00bb0f00` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0f04"></a> `00bb0f04` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0f08"></a> `00bb0f08` | `08 a1 4a 39` | ldrb w8,[x8, #0x2a8] | `FALL_THROUGH`
<a id="insn-00bb0f0c"></a> `00bb0f0c` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0f24 | `CONDITIONAL_JUMP`
<a id="insn-00bb0f10"></a> `00bb0f10` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0f14"></a> `00bb0f14` | `08 a1 0a 91` | add x8,x8,#0x2a8 | `FALL_THROUGH`
<a id="insn-00bb0f18"></a> `00bb0f18` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0f1c"></a> `00bb0f1c` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0f20"></a> `00bb0f20` | `06 00 00 14` | b 0x00bb0f38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0f24"></a> `00bb0f24` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0f28"></a> `00bb0f28` | `29 c1 0a 91` | add x9,x9,#0x2b0 | `FALL_THROUGH`
<a id="insn-00bb0f2c"></a> `00bb0f2c` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0f30"></a> `00bb0f30` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0f34"></a> `00bb0f34` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0f38"></a> `00bb0f38` | `c9 09 80 d2` | mov x9,#0x4e | `FALL_THROUGH`
<a id="insn-00bb0f3c"></a> `00bb0f3c` | `ca 0e 80 52` | mov w10,#0x76 | `FALL_THROUGH`
<a id="insn-00bb0f40"></a> `00bb0f40` | `e9 0d c0 f2` | movk x9,#0x6f, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0f44"></a> `00bb0f44` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0f48"></a> `00bb0f48` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0f4c"></a> `00bb0f4c` | `08 01 4b 39` | ldrb w8,[x8, #0x2c0] | `FALL_THROUGH`
<a id="insn-00bb0f50"></a> `00bb0f50` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0f68 | `CONDITIONAL_JUMP`
<a id="insn-00bb0f54"></a> `00bb0f54` | `88 27 00 f0` | adrp x8,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0f58"></a> `00bb0f58` | `08 01 0b 91` | add x8,x8,#0x2c0 | `FALL_THROUGH`
<a id="insn-00bb0f5c"></a> `00bb0f5c` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0f60"></a> `00bb0f60` | `09 45 00 38` | strb w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb0f64"></a> `00bb0f64` | `06 00 00 14` | b 0x00bb0f7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0f68"></a> `00bb0f68` | `89 27 00 f0` | adrp x9,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0f6c"></a> `00bb0f6c` | `29 21 0b 91` | add x9,x9,#0x2c8 | `FALL_THROUGH`
<a id="insn-00bb0f70"></a> `00bb0f70` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb0f74"></a> `00bb0f74` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0f78"></a> `00bb0f78` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0f7c"></a> `00bb0f7c` | `89 08 80 d2` | mov x9,#0x44 | `FALL_THROUGH`
<a id="insn-00bb0f80"></a> `00bb0f80` | `6a 0c 80 52` | mov w10,#0x63 | `FALL_THROUGH`
<a id="insn-00bb0f84"></a> `00bb0f84` | `a9 0c c0 f2` | movk x9,#0x65, LSL #32 | `FALL_THROUGH`
<a id="insn-00bb0f88"></a> `00bb0f88` | `09 29 00 a9` | stp x9,x10,[x8] | `FALL_THROUGH`
<a id="insn-00bb0f8c"></a> `00bb0f8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0f90"></a> `00bb0f90` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb0f94"></a> `00bb0f94` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb0f98"></a> `00bb0f98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb0f9c"></a> `00bb0f9c` | `80 27 00 f0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0fa0"></a> `00bb0fa0` | `00 60 0b 91` | add x0,x0,#0x2d8 | `FALL_THROUGH`
<a id="insn-00bb0fa4"></a> `00bb0fa4` | `d7 a7 00 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0fa8"></a> `00bb0fa8` | `20 d9 ff 34` | cbz w0,0x00bb0acc | `CONDITIONAL_JUMP`
<a id="insn-00bb0fac"></a> `00bb0fac` | `40 00 00 90` | adrp x0,0xbb8000 | `FALL_THROUGH`
<a id="insn-00bb0fb0"></a> `00bb0fb0` | `00 50 3d 91` | add x0,x0,#0xf54 | `FALL_THROUGH`
<a id="insn-00bb0fb4"></a> `00bb0fb4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bb0fb8"></a> `00bb0fb8` | `c2 78 1a 10` | adr x2,0xbe5ed0 | `FALL_THROUGH`
<a id="insn-00bb0fbc"></a> `00bb0fbc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bb0fc0"></a> `00bb0fc0` | `c8 a7 00 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0fc4"></a> `00bb0fc4` | `80 27 00 f0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bb0fc8"></a> `00bb0fc8` | `00 60 0b 91` | add x0,x0,#0x2d8 | `FALL_THROUGH`
<a id="insn-00bb0fcc"></a> `00bb0fcc` | `d5 a7 00 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0fd0"></a> `00bb0fd0` | `bf fe ff 17` | b 0x00bb0acc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bb0aac`](#insn-00bb0aac) 範囲 `[['00bb0aac', '00bb0acb']]`
  - `CONDITIONAL_JUMP` [`00bb0ac8`](#insn-00bb0ac8) → [`00bb0f9c`](#insn-00bb0f9c)
  - `FALL_THROUGH` [`00bb0ac8`](#insn-00bb0ac8) → [`00bb0acc`](#insn-00bb0acc)
- ブロック [`00bb0acc`](#insn-00bb0acc) 範囲 `[['00bb0acc', '00bb0b2b']]`
  - `CONDITIONAL_JUMP` [`00bb0b28`](#insn-00bb0b28) → [`00bb0b40`](#insn-00bb0b40)
  - `FALL_THROUGH` [`00bb0b28`](#insn-00bb0b28) → [`00bb0b2c`](#insn-00bb0b2c)
- ブロック [`00bb0b2c`](#insn-00bb0b2c) 範囲 `[['00bb0b2c', '00bb0b3f']]`
  - `UNCONDITIONAL_JUMP` [`00bb0b3c`](#insn-00bb0b3c) → [`00bb0b54`](#insn-00bb0b54)
- ブロック [`00bb0b40`](#insn-00bb0b40) 範囲 `[['00bb0b40', '00bb0b53']]`
  - `FALL_THROUGH` [`00bb0b50`](#insn-00bb0b50) → [`00bb0b54`](#insn-00bb0b54)
- ブロック [`00bb0b54`](#insn-00bb0b54) 範囲 `[['00bb0b54', '00bb0b6f']]`
  - `CONDITIONAL_JUMP` [`00bb0b6c`](#insn-00bb0b6c) → [`00bb0b84`](#insn-00bb0b84)
  - `FALL_THROUGH` [`00bb0b6c`](#insn-00bb0b6c) → [`00bb0b70`](#insn-00bb0b70)
- ブロック [`00bb0b70`](#insn-00bb0b70) 範囲 `[['00bb0b70', '00bb0b83']]`
  - `UNCONDITIONAL_JUMP` [`00bb0b80`](#insn-00bb0b80) → [`00bb0b98`](#insn-00bb0b98)
- ブロック [`00bb0b84`](#insn-00bb0b84) 範囲 `[['00bb0b84', '00bb0b97']]`
  - `FALL_THROUGH` [`00bb0b94`](#insn-00bb0b94) → [`00bb0b98`](#insn-00bb0b98)
- ブロック [`00bb0b98`](#insn-00bb0b98) 範囲 `[['00bb0b98', '00bb0b9b']]`
  - `FALL_THROUGH` [`00bb0b98`](#insn-00bb0b98) → [`00bb0b9c`](#insn-00bb0b9c)
- ブロック [`00bb0b9c`](#insn-00bb0b9c) 範囲 `[['00bb0b9c', '00bb0bb7']]`
  - `CONDITIONAL_JUMP` [`00bb0bb4`](#insn-00bb0bb4) → [`00bb0bcc`](#insn-00bb0bcc)
  - `FALL_THROUGH` [`00bb0bb4`](#insn-00bb0bb4) → [`00bb0bb8`](#insn-00bb0bb8)
- ブロック [`00bb0bb8`](#insn-00bb0bb8) 範囲 `[['00bb0bb8', '00bb0bcb']]`
  - `UNCONDITIONAL_JUMP` [`00bb0bc8`](#insn-00bb0bc8) → [`00bb0be0`](#insn-00bb0be0)
- ブロック [`00bb0bcc`](#insn-00bb0bcc) 範囲 `[['00bb0bcc', '00bb0bdf']]`
  - `FALL_THROUGH` [`00bb0bdc`](#insn-00bb0bdc) → [`00bb0be0`](#insn-00bb0be0)
- ブロック [`00bb0be0`](#insn-00bb0be0) 範囲 `[['00bb0be0', '00bb0c67']]`
  - `FALL_THROUGH` [`00bb0c64`](#insn-00bb0c64) → [`00bb0c68`](#insn-00bb0c68)
- ブロック [`00bb0c68`](#insn-00bb0c68) 範囲 `[['00bb0c68', '00bb0c6b']]`
  - `CONDITIONAL_JUMP` [`00bb0c68`](#insn-00bb0c68) → [`00bb0c7c`](#insn-00bb0c7c)
  - `FALL_THROUGH` [`00bb0c68`](#insn-00bb0c68) → [`00bb0c6c`](#insn-00bb0c6c)
- ブロック [`00bb0c6c`](#insn-00bb0c6c) 範囲 `[['00bb0c6c', '00bb0c7b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0c78`](#insn-00bb0c78) → [`00bb0c90`](#insn-00bb0c90)
- ブロック [`00bb0c7c`](#insn-00bb0c7c) 範囲 `[['00bb0c7c', '00bb0c8f']]`
  - `FALL_THROUGH` [`00bb0c8c`](#insn-00bb0c8c) → [`00bb0c90`](#insn-00bb0c90)
- ブロック [`00bb0c90`](#insn-00bb0c90) 範囲 `[['00bb0c90', '00bb0c9b']]`
  - `FALL_THROUGH` [`00bb0c98`](#insn-00bb0c98) → [`00bb0c9c`](#insn-00bb0c9c)
- ブロック [`00bb0c9c`](#insn-00bb0c9c) 範囲 `[['00bb0c9c', '00bb0cab']]`
  - `CONDITIONAL_JUMP` [`00bb0ca8`](#insn-00bb0ca8) → [`00bb0cc0`](#insn-00bb0cc0)
  - `FALL_THROUGH` [`00bb0ca8`](#insn-00bb0ca8) → [`00bb0cac`](#insn-00bb0cac)
- ブロック [`00bb0cac`](#insn-00bb0cac) 範囲 `[['00bb0cac', '00bb0cbb']]`
  - `FALL_THROUGH` [`00bb0cb8`](#insn-00bb0cb8) → [`00bb0cbc`](#insn-00bb0cbc)
- ブロック [`00bb0cbc`](#insn-00bb0cbc) 範囲 `[['00bb0cbc', '00bb0cbf']]`
  - `UNCONDITIONAL_JUMP` [`00bb0cbc`](#insn-00bb0cbc) → [`00bb0cd4`](#insn-00bb0cd4)
- ブロック [`00bb0cc0`](#insn-00bb0cc0) 範囲 `[['00bb0cc0', '00bb0cd3']]`
  - `FALL_THROUGH` [`00bb0cd0`](#insn-00bb0cd0) → [`00bb0cd4`](#insn-00bb0cd4)
- ブロック [`00bb0cd4`](#insn-00bb0cd4) 範囲 `[['00bb0cd4', '00bb0cdb']]`
  - `FALL_THROUGH` [`00bb0cd8`](#insn-00bb0cd8) → [`00bb0cdc`](#insn-00bb0cdc)
- ブロック [`00bb0cdc`](#insn-00bb0cdc) 範囲 `[['00bb0cdc', '00bb0cdf']]`
  - `FALL_THROUGH` [`00bb0cdc`](#insn-00bb0cdc) → [`00bb0ce0`](#insn-00bb0ce0)
- ブロック [`00bb0ce0`](#insn-00bb0ce0) 範囲 `[['00bb0ce0', '00bb0ce3']]`
  - `FALL_THROUGH` [`00bb0ce0`](#insn-00bb0ce0) → [`00bb0ce4`](#insn-00bb0ce4)
- ブロック [`00bb0ce4`](#insn-00bb0ce4) 範囲 `[['00bb0ce4', '00bb0ce7']]`
  - `FALL_THROUGH` [`00bb0ce4`](#insn-00bb0ce4) → [`00bb0ce8`](#insn-00bb0ce8)
- ブロック [`00bb0ce8`](#insn-00bb0ce8) 範囲 `[['00bb0ce8', '00bb0ceb']]`
  - `FALL_THROUGH` [`00bb0ce8`](#insn-00bb0ce8) → [`00bb0cec`](#insn-00bb0cec)
- ブロック [`00bb0cec`](#insn-00bb0cec) 範囲 `[['00bb0cec', '00bb0cef']]`
  - `CONDITIONAL_JUMP` [`00bb0cec`](#insn-00bb0cec) → [`00bb0d04`](#insn-00bb0d04)
  - `FALL_THROUGH` [`00bb0cec`](#insn-00bb0cec) → [`00bb0cf0`](#insn-00bb0cf0)
- ブロック [`00bb0cf0`](#insn-00bb0cf0) 範囲 `[['00bb0cf0', '00bb0cf3']]`
  - `FALL_THROUGH` [`00bb0cf0`](#insn-00bb0cf0) → [`00bb0cf4`](#insn-00bb0cf4)
- ブロック [`00bb0cf4`](#insn-00bb0cf4) 範囲 `[['00bb0cf4', '00bb0cf7']]`
  - `FALL_THROUGH` [`00bb0cf4`](#insn-00bb0cf4) → [`00bb0cf8`](#insn-00bb0cf8)
- ブロック [`00bb0cf8`](#insn-00bb0cf8) 範囲 `[['00bb0cf8', '00bb0cfb']]`
  - `FALL_THROUGH` [`00bb0cf8`](#insn-00bb0cf8) → [`00bb0cfc`](#insn-00bb0cfc)
- ブロック [`00bb0cfc`](#insn-00bb0cfc) 範囲 `[['00bb0cfc', '00bb0cff']]`
  - `FALL_THROUGH` [`00bb0cfc`](#insn-00bb0cfc) → [`00bb0d00`](#insn-00bb0d00)
- ブロック [`00bb0d00`](#insn-00bb0d00) 範囲 `[['00bb0d00', '00bb0d03']]`
  - `UNCONDITIONAL_JUMP` [`00bb0d00`](#insn-00bb0d00) → [`00bb0d18`](#insn-00bb0d18)
- ブロック [`00bb0d04`](#insn-00bb0d04) 範囲 `[['00bb0d04', '00bb0d07']]`
  - `FALL_THROUGH` [`00bb0d04`](#insn-00bb0d04) → [`00bb0d08`](#insn-00bb0d08)
- ブロック [`00bb0d08`](#insn-00bb0d08) 範囲 `[['00bb0d08', '00bb0d0b']]`
  - `FALL_THROUGH` [`00bb0d08`](#insn-00bb0d08) → [`00bb0d0c`](#insn-00bb0d0c)
- ブロック [`00bb0d0c`](#insn-00bb0d0c) 範囲 `[['00bb0d0c', '00bb0d13']]`
  - `FALL_THROUGH` [`00bb0d10`](#insn-00bb0d10) → [`00bb0d14`](#insn-00bb0d14)
- ブロック [`00bb0d14`](#insn-00bb0d14) 範囲 `[['00bb0d14', '00bb0d17']]`
  - `FALL_THROUGH` [`00bb0d14`](#insn-00bb0d14) → [`00bb0d18`](#insn-00bb0d18)
- ブロック [`00bb0d18`](#insn-00bb0d18) 範囲 `[['00bb0d18', '00bb0d1b']]`
  - `FALL_THROUGH` [`00bb0d18`](#insn-00bb0d18) → [`00bb0d1c`](#insn-00bb0d1c)
- ブロック [`00bb0d1c`](#insn-00bb0d1c) 範囲 `[['00bb0d1c', '00bb0d1f']]`
  - `FALL_THROUGH` [`00bb0d1c`](#insn-00bb0d1c) → [`00bb0d20`](#insn-00bb0d20)
- ブロック [`00bb0d20`](#insn-00bb0d20) 範囲 `[['00bb0d20', '00bb0d23']]`
  - `FALL_THROUGH` [`00bb0d20`](#insn-00bb0d20) → [`00bb0d24`](#insn-00bb0d24)
- ブロック [`00bb0d24`](#insn-00bb0d24) 範囲 `[['00bb0d24', '00bb0d27']]`
  - `FALL_THROUGH` [`00bb0d24`](#insn-00bb0d24) → [`00bb0d28`](#insn-00bb0d28)
- ブロック [`00bb0d28`](#insn-00bb0d28) 範囲 `[['00bb0d28', '00bb0d2b']]`
  - `FALL_THROUGH` [`00bb0d28`](#insn-00bb0d28) → [`00bb0d2c`](#insn-00bb0d2c)
- ブロック [`00bb0d2c`](#insn-00bb0d2c) 範囲 `[['00bb0d2c', '00bb0d33']]`
  - `CONDITIONAL_JUMP` [`00bb0d30`](#insn-00bb0d30) → [`00bb0d48`](#insn-00bb0d48)
  - `FALL_THROUGH` [`00bb0d30`](#insn-00bb0d30) → [`00bb0d34`](#insn-00bb0d34)
- ブロック [`00bb0d34`](#insn-00bb0d34) 範囲 `[['00bb0d34', '00bb0d47']]`
  - `UNCONDITIONAL_JUMP` [`00bb0d44`](#insn-00bb0d44) → [`00bb0d5c`](#insn-00bb0d5c)
- ブロック [`00bb0d48`](#insn-00bb0d48) 範囲 `[['00bb0d48', '00bb0d5b']]`
  - `FALL_THROUGH` [`00bb0d58`](#insn-00bb0d58) → [`00bb0d5c`](#insn-00bb0d5c)
- ブロック [`00bb0d5c`](#insn-00bb0d5c) 範囲 `[['00bb0d5c', '00bb0d77']]`
  - `CONDITIONAL_JUMP` [`00bb0d74`](#insn-00bb0d74) → [`00bb0d8c`](#insn-00bb0d8c)
  - `FALL_THROUGH` [`00bb0d74`](#insn-00bb0d74) → [`00bb0d78`](#insn-00bb0d78)
- ブロック [`00bb0d78`](#insn-00bb0d78) 範囲 `[['00bb0d78', '00bb0d8b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0d88`](#insn-00bb0d88) → [`00bb0da0`](#insn-00bb0da0)
- ブロック [`00bb0d8c`](#insn-00bb0d8c) 範囲 `[['00bb0d8c', '00bb0d97']]`
  - `FALL_THROUGH` [`00bb0d94`](#insn-00bb0d94) → [`00bb0d98`](#insn-00bb0d98)
- ブロック [`00bb0d98`](#insn-00bb0d98) 範囲 `[['00bb0d98', '00bb0d9f']]`
  - `FALL_THROUGH` [`00bb0d9c`](#insn-00bb0d9c) → [`00bb0da0`](#insn-00bb0da0)
- ブロック [`00bb0da0`](#insn-00bb0da0) 範囲 `[['00bb0da0', '00bb0dbb']]`
  - `CONDITIONAL_JUMP` [`00bb0db8`](#insn-00bb0db8) → [`00bb0dd0`](#insn-00bb0dd0)
  - `FALL_THROUGH` [`00bb0db8`](#insn-00bb0db8) → [`00bb0dbc`](#insn-00bb0dbc)
- ブロック [`00bb0dbc`](#insn-00bb0dbc) 範囲 `[['00bb0dbc', '00bb0dcf']]`
  - `UNCONDITIONAL_JUMP` [`00bb0dcc`](#insn-00bb0dcc) → [`00bb0de4`](#insn-00bb0de4)
- ブロック [`00bb0dd0`](#insn-00bb0dd0) 範囲 `[['00bb0dd0', '00bb0de3']]`
  - `FALL_THROUGH` [`00bb0de0`](#insn-00bb0de0) → [`00bb0de4`](#insn-00bb0de4)
- ブロック [`00bb0de4`](#insn-00bb0de4) 範囲 `[['00bb0de4', '00bb0dff']]`
  - `CONDITIONAL_JUMP` [`00bb0dfc`](#insn-00bb0dfc) → [`00bb0e14`](#insn-00bb0e14)
  - `FALL_THROUGH` [`00bb0dfc`](#insn-00bb0dfc) → [`00bb0e00`](#insn-00bb0e00)
- ブロック [`00bb0e00`](#insn-00bb0e00) 範囲 `[['00bb0e00', '00bb0e13']]`
  - `UNCONDITIONAL_JUMP` [`00bb0e10`](#insn-00bb0e10) → [`00bb0e28`](#insn-00bb0e28)
- ブロック [`00bb0e14`](#insn-00bb0e14) 範囲 `[['00bb0e14', '00bb0e27']]`
  - `FALL_THROUGH` [`00bb0e24`](#insn-00bb0e24) → [`00bb0e28`](#insn-00bb0e28)
- ブロック [`00bb0e28`](#insn-00bb0e28) 範囲 `[['00bb0e28', '00bb0e43']]`
  - `CONDITIONAL_JUMP` [`00bb0e40`](#insn-00bb0e40) → [`00bb0e58`](#insn-00bb0e58)
  - `FALL_THROUGH` [`00bb0e40`](#insn-00bb0e40) → [`00bb0e44`](#insn-00bb0e44)
- ブロック [`00bb0e44`](#insn-00bb0e44) 範囲 `[['00bb0e44', '00bb0e57']]`
  - `UNCONDITIONAL_JUMP` [`00bb0e54`](#insn-00bb0e54) → [`00bb0e6c`](#insn-00bb0e6c)
- ブロック [`00bb0e58`](#insn-00bb0e58) 範囲 `[['00bb0e58', '00bb0e6b']]`
  - `FALL_THROUGH` [`00bb0e68`](#insn-00bb0e68) → [`00bb0e6c`](#insn-00bb0e6c)
- ブロック [`00bb0e6c`](#insn-00bb0e6c) 範囲 `[['00bb0e6c', '00bb0e87']]`
  - `CONDITIONAL_JUMP` [`00bb0e84`](#insn-00bb0e84) → [`00bb0e9c`](#insn-00bb0e9c)
  - `FALL_THROUGH` [`00bb0e84`](#insn-00bb0e84) → [`00bb0e88`](#insn-00bb0e88)
- ブロック [`00bb0e88`](#insn-00bb0e88) 範囲 `[['00bb0e88', '00bb0e9b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0e98`](#insn-00bb0e98) → [`00bb0eb0`](#insn-00bb0eb0)
- ブロック [`00bb0e9c`](#insn-00bb0e9c) 範囲 `[['00bb0e9c', '00bb0eaf']]`
  - `FALL_THROUGH` [`00bb0eac`](#insn-00bb0eac) → [`00bb0eb0`](#insn-00bb0eb0)
- ブロック [`00bb0eb0`](#insn-00bb0eb0) 範囲 `[['00bb0eb0', '00bb0ecb']]`
  - `CONDITIONAL_JUMP` [`00bb0ec8`](#insn-00bb0ec8) → [`00bb0ee0`](#insn-00bb0ee0)
  - `FALL_THROUGH` [`00bb0ec8`](#insn-00bb0ec8) → [`00bb0ecc`](#insn-00bb0ecc)
- ブロック [`00bb0ecc`](#insn-00bb0ecc) 範囲 `[['00bb0ecc', '00bb0edf']]`
  - `UNCONDITIONAL_JUMP` [`00bb0edc`](#insn-00bb0edc) → [`00bb0ef4`](#insn-00bb0ef4)
- ブロック [`00bb0ee0`](#insn-00bb0ee0) 範囲 `[['00bb0ee0', '00bb0eeb']]`
  - `FALL_THROUGH` [`00bb0ee8`](#insn-00bb0ee8) → [`00bb0eec`](#insn-00bb0eec)
- ブロック [`00bb0eec`](#insn-00bb0eec) 範囲 `[['00bb0eec', '00bb0ef3']]`
  - `FALL_THROUGH` [`00bb0ef0`](#insn-00bb0ef0) → [`00bb0ef4`](#insn-00bb0ef4)
- ブロック [`00bb0ef4`](#insn-00bb0ef4) 範囲 `[['00bb0ef4', '00bb0f0f']]`
  - `CONDITIONAL_JUMP` [`00bb0f0c`](#insn-00bb0f0c) → [`00bb0f24`](#insn-00bb0f24)
  - `FALL_THROUGH` [`00bb0f0c`](#insn-00bb0f0c) → [`00bb0f10`](#insn-00bb0f10)
- ブロック [`00bb0f10`](#insn-00bb0f10) 範囲 `[['00bb0f10', '00bb0f23']]`
  - `UNCONDITIONAL_JUMP` [`00bb0f20`](#insn-00bb0f20) → [`00bb0f38`](#insn-00bb0f38)
- ブロック [`00bb0f24`](#insn-00bb0f24) 範囲 `[['00bb0f24', '00bb0f37']]`
  - `FALL_THROUGH` [`00bb0f34`](#insn-00bb0f34) → [`00bb0f38`](#insn-00bb0f38)
- ブロック [`00bb0f38`](#insn-00bb0f38) 範囲 `[['00bb0f38', '00bb0f53']]`
  - `CONDITIONAL_JUMP` [`00bb0f50`](#insn-00bb0f50) → [`00bb0f68`](#insn-00bb0f68)
  - `FALL_THROUGH` [`00bb0f50`](#insn-00bb0f50) → [`00bb0f54`](#insn-00bb0f54)
- ブロック [`00bb0f54`](#insn-00bb0f54) 範囲 `[['00bb0f54', '00bb0f67']]`
  - `UNCONDITIONAL_JUMP` [`00bb0f64`](#insn-00bb0f64) → [`00bb0f7c`](#insn-00bb0f7c)
- ブロック [`00bb0f68`](#insn-00bb0f68) 範囲 `[['00bb0f68', '00bb0f73']]`
  - `FALL_THROUGH` [`00bb0f70`](#insn-00bb0f70) → [`00bb0f74`](#insn-00bb0f74)
- ブロック [`00bb0f74`](#insn-00bb0f74) 範囲 `[['00bb0f74', '00bb0f7b']]`
  - `FALL_THROUGH` [`00bb0f78`](#insn-00bb0f78) → [`00bb0f7c`](#insn-00bb0f7c)
- ブロック [`00bb0f7c`](#insn-00bb0f7c) 範囲 `[['00bb0f7c', '00bb0f9b']]`
- ブロック [`00bb0f9c`](#insn-00bb0f9c) 範囲 `[['00bb0f9c', '00bb0fab']]`
  - `CONDITIONAL_JUMP` [`00bb0fa8`](#insn-00bb0fa8) → [`00bb0acc`](#insn-00bb0acc)
  - `FALL_THROUGH` [`00bb0fa8`](#insn-00bb0fa8) → [`00bb0fac`](#insn-00bb0fac)
- ブロック [`00bb0fac`](#insn-00bb0fac) 範囲 `[['00bb0fac', '00bb0fd3']]`
  - `UNCONDITIONAL_JUMP` [`00bb0fd0`](#insn-00bb0fd0) → [`00bb0acc`](#insn-00bb0acc)

## 命令位置別の参照

- [`00bb0ab0`](#insn-00bb0ab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ab4`](#insn-00bb0ab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ac4`](#insn-00bb0ac4) → `010a32d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0ac8`](#insn-00bb0ac8) → [`00bb0f9c`](#insn-00bb0f9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ad8`](#insn-00bb0ad8) → `002fa6cc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0adc`](#insn-00bb0adc) → `010a3098`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ae4`](#insn-00bb0ae4) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0aec`](#insn-00bb0aec) → `002fa87c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0af0`](#insn-00bb0af0) → `010a30b0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0af8`](#insn-00bb0af8) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b00`](#insn-00bb0b00) → `002fa954`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0b04`](#insn-00bb0b04) → `010a30c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b0c`](#insn-00bb0b0c) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b14`](#insn-00bb0b14) → `002fa748`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0b18`](#insn-00bb0b18) → `010a30e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b20`](#insn-00bb0b20) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b24`](#insn-00bb0b24) → `010a30f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0b28`](#insn-00bb0b28) → [`00bb0b40`](#insn-00bb0b40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b38`](#insn-00bb0b38) → `010a30f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0b3c`](#insn-00bb0b3c) → [`00bb0b54`](#insn-00bb0b54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b4c`](#insn-00bb0b4c) → `010a3108`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0b50`](#insn-00bb0b50) → `010a3100`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0b60`](#insn-00bb0b60) → `010a30fc`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0b60`](#insn-00bb0b60) → `010a3104`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0b68`](#insn-00bb0b68) → `010a3110`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0b6c`](#insn-00bb0b6c) → [`00bb0b84`](#insn-00bb0b84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b7c`](#insn-00bb0b7c) → `010a3110`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0b80`](#insn-00bb0b80) → [`00bb0b98`](#insn-00bb0b98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0b90`](#insn-00bb0b90) → `010a3120`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0b94`](#insn-00bb0b94) → `010a3118`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ba0`](#insn-00bb0ba0) → `010a3124`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ba4`](#insn-00bb0ba4) → `002fa96c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ba8`](#insn-00bb0ba8) → `010a3114`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0bb0`](#insn-00bb0bb0) → `010a3128`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0bb4`](#insn-00bb0bb4) → [`00bb0bcc`](#insn-00bb0bcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0bc4`](#insn-00bb0bc4) → `010a3128`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0bc8`](#insn-00bb0bc8) → [`00bb0be0`](#insn-00bb0be0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0bd8`](#insn-00bb0bd8) → `010a3138`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0bdc`](#insn-00bb0bdc) → `010a3130`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0bf0`](#insn-00bb0bf0) → `002fa6b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0bf8`](#insn-00bb0bf8) → `002fa660`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0bfc`](#insn-00bb0bfc) → `010a3140`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c04`](#insn-00bb0c04) → `010a312c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c0c`](#insn-00bb0c0c) → `010a313c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0c10`](#insn-00bb0c10) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c18`](#insn-00bb0c18) → `002fa6fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0c1c`](#insn-00bb0c1c) → `010a3158`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c24`](#insn-00bb0c24) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c2c`](#insn-00bb0c2c) → `002fa8a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0c30`](#insn-00bb0c30) → `010a3170`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c38`](#insn-00bb0c38) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c40`](#insn-00bb0c40) → `002fa7a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0c44`](#insn-00bb0c44) → `010a3188`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c4c`](#insn-00bb0c4c) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c54`](#insn-00bb0c54) → `002fa724`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `unicode32`
- [`00bb0c58`](#insn-00bb0c58) → `010a31a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c60`](#insn-00bb0c60) → [`00b76424`](../00b76/00b76424.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b76424` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c64`](#insn-00bb0c64) → `010a31b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0c68`](#insn-00bb0c68) → [`00bb0c7c`](#insn-00bb0c7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c74`](#insn-00bb0c74) → `010a31b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0c78`](#insn-00bb0c78) → [`00bb0c90`](#insn-00bb0c90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0c88`](#insn-00bb0c88) → `010a31c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0c8c`](#insn-00bb0c8c) → `010a31c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0c9c`](#insn-00bb0c9c) → `010a31bc`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0c9c`](#insn-00bb0c9c) → `010a31c4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ca4`](#insn-00bb0ca4) → `010a31d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0ca8`](#insn-00bb0ca8) → [`00bb0cc0`](#insn-00bb0cc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0cb8`](#insn-00bb0cb8) → `010a31d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0cbc`](#insn-00bb0cbc) → [`00bb0cd4`](#insn-00bb0cd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ccc`](#insn-00bb0ccc) → `010a31e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0cd0`](#insn-00bb0cd0) → `010a31d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ce0`](#insn-00bb0ce0) → `010a31d4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ce0`](#insn-00bb0ce0) → `010a31dc`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ce8`](#insn-00bb0ce8) → `010a31e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0cec`](#insn-00bb0cec) → [`00bb0d04`](#insn-00bb0d04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0cfc`](#insn-00bb0cfc) → `010a31e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0d00`](#insn-00bb0d00) → [`00bb0d18`](#insn-00bb0d18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0d10`](#insn-00bb0d10) → `010a31f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d14`](#insn-00bb0d14) → `010a31f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d24`](#insn-00bb0d24) → `010a31ec`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d24`](#insn-00bb0d24) → `010a31f4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d2c`](#insn-00bb0d2c) → `010a3200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0d30`](#insn-00bb0d30) → [`00bb0d48`](#insn-00bb0d48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0d40`](#insn-00bb0d40) → `010a3200`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0d44`](#insn-00bb0d44) → [`00bb0d5c`](#insn-00bb0d5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0d54`](#insn-00bb0d54) → `010a3210`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d58`](#insn-00bb0d58) → `010a3208`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d68`](#insn-00bb0d68) → `010a3204`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d68`](#insn-00bb0d68) → `010a320c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d70`](#insn-00bb0d70) → `010a3218`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0d74`](#insn-00bb0d74) → [`00bb0d8c`](#insn-00bb0d8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0d84`](#insn-00bb0d84) → `010a3218`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0d88`](#insn-00bb0d88) → [`00bb0da0`](#insn-00bb0da0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0d98`](#insn-00bb0d98) → `010a3228`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0d9c`](#insn-00bb0d9c) → `010a3220`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0dac`](#insn-00bb0dac) → `010a321c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0dac`](#insn-00bb0dac) → `010a3224`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0db4`](#insn-00bb0db4) → `010a3230`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0db8`](#insn-00bb0db8) → [`00bb0dd0`](#insn-00bb0dd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0dc8`](#insn-00bb0dc8) → `010a3230`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0dcc`](#insn-00bb0dcc) → [`00bb0de4`](#insn-00bb0de4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ddc`](#insn-00bb0ddc) → `010a3240`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0de0`](#insn-00bb0de0) → `010a3238`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0df0`](#insn-00bb0df0) → `010a3234`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0df0`](#insn-00bb0df0) → `010a323c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0df8`](#insn-00bb0df8) → `010a3248`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0dfc`](#insn-00bb0dfc) → [`00bb0e14`](#insn-00bb0e14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0e0c`](#insn-00bb0e0c) → `010a3248`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0e10`](#insn-00bb0e10) → [`00bb0e28`](#insn-00bb0e28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0e20`](#insn-00bb0e20) → `010a3258`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e24`](#insn-00bb0e24) → `010a3250`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e34`](#insn-00bb0e34) → `010a324c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e34`](#insn-00bb0e34) → `010a3254`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e3c`](#insn-00bb0e3c) → `010a3260`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0e40`](#insn-00bb0e40) → [`00bb0e58`](#insn-00bb0e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0e50`](#insn-00bb0e50) → `010a3260`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0e54`](#insn-00bb0e54) → [`00bb0e6c`](#insn-00bb0e6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0e64`](#insn-00bb0e64) → `010a3270`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e68`](#insn-00bb0e68) → `010a3268`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e78`](#insn-00bb0e78) → `010a3264`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e78`](#insn-00bb0e78) → `010a326c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0e80`](#insn-00bb0e80) → `010a3278`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0e84`](#insn-00bb0e84) → [`00bb0e9c`](#insn-00bb0e9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0e94`](#insn-00bb0e94) → `010a3278`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0e98`](#insn-00bb0e98) → [`00bb0eb0`](#insn-00bb0eb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ea8`](#insn-00bb0ea8) → `010a3288`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0eac`](#insn-00bb0eac) → `010a3280`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ebc`](#insn-00bb0ebc) → `010a327c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ebc`](#insn-00bb0ebc) → `010a3284`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ec4`](#insn-00bb0ec4) → `010a3290`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0ec8`](#insn-00bb0ec8) → [`00bb0ee0`](#insn-00bb0ee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0ed8`](#insn-00bb0ed8) → `010a3290`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0edc`](#insn-00bb0edc) → [`00bb0ef4`](#insn-00bb0ef4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0eec`](#insn-00bb0eec) → `010a32a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0ef0`](#insn-00bb0ef0) → `010a3298`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f00`](#insn-00bb0f00) → `010a3294`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f00`](#insn-00bb0f00) → `010a329c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f08`](#insn-00bb0f08) → `010a32a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0f0c`](#insn-00bb0f0c) → [`00bb0f24`](#insn-00bb0f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0f1c`](#insn-00bb0f1c) → `010a32a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0f20`](#insn-00bb0f20) → [`00bb0f38`](#insn-00bb0f38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0f30`](#insn-00bb0f30) → `010a32b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f34`](#insn-00bb0f34) → `010a32b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f44`](#insn-00bb0f44) → `010a32ac`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f44`](#insn-00bb0f44) → `010a32b4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f4c`](#insn-00bb0f4c) → `010a32c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0f50`](#insn-00bb0f50) → [`00bb0f68`](#insn-00bb0f68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0f60`](#insn-00bb0f60) → `010a32c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0f64`](#insn-00bb0f64) → [`00bb0f7c`](#insn-00bb0f7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0f74`](#insn-00bb0f74) → `010a32d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f78`](#insn-00bb0f78) → `010a32c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f88`](#insn-00bb0f88) → `010a32c4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f88`](#insn-00bb0f88) → `010a32cc`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0f8c`](#insn-00bb0f8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0f90`](#insn-00bb0f90) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0fa0`](#insn-00bb0fa0) → `010a32d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0fa4`](#insn-00bb0fa4) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00bb0fa8`](#insn-00bb0fa8) → [`00bb0acc`](#insn-00bb0acc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0fb0`](#insn-00bb0fb0) → [`00bb8f54`](../00bb8/00bb8f54.md) · `PARAM` · `ANALYSIS` · 関数 `00bb8f54` · 推定シンボル `None` · 推定型 `None`
- [`00bb0fb8`](#insn-00bb0fb8) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb0fc0`](#insn-00bb0fc0) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00bb0fc8`](#insn-00bb0fc8) → `010a32d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0fcc`](#insn-00bb0fcc) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00bb0fd0`](#insn-00bb0fd0) → [`00bb0acc`](#insn-00bb0acc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb0ab0`](#insn-00bb0ab0)

~~~json
{
  "source": "00bb0ab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ab4`](#insn-00bb0ab4)

~~~json
{
  "source": "00bb0ab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ac4`](#insn-00bb0ac4)

~~~json
{
  "source": "00bb0ac4",
  "target": "010a32d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ac8`](#insn-00bb0ac8)

~~~json
{
  "source": "00bb0ac8",
  "target": "00bb0f9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ad8`](#insn-00bb0ad8)

~~~json
{
  "source": "00bb0ad8",
  "target": "002fa6cc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa6cc",
  "offset": 0,
  "size": 32,
  "datatype": "unicode32",
  "bytes": "4a000000610000006e0000007500000061000000720000007900000000000000",
  "capture_start": "002fa6cc",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb0adc`](#insn-00bb0adc)

~~~json
{
  "source": "00bb0adc",
  "target": "010a3098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ae4`](#insn-00bb0ae4)

~~~json
{
  "source": "00bb0ae4",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0aec`](#insn-00bb0aec)

~~~json
{
  "source": "00bb0aec",
  "target": "002fa87c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa87c",
  "offset": 0,
  "size": 36,
  "datatype": "unicode32",
  "bytes": "4600000065000000620000007200000075000000610000007200000079000000",
  "capture_start": "002fa87c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb0af0`](#insn-00bb0af0)

~~~json
{
  "source": "00bb0af0",
  "target": "010a30b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0af8`](#insn-00bb0af8)

~~~json
{
  "source": "00bb0af8",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0b00`](#insn-00bb0b00)

~~~json
{
  "source": "00bb0b00",
  "target": "002fa954",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa954",
  "offset": 0,
  "size": 24,
  "datatype": "unicode32",
  "bytes": "4d0000006100000072000000630000006800000000000000",
  "capture_start": "002fa954",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb0b04`](#insn-00bb0b04)

~~~json
{
  "source": "00bb0b04",
  "target": "010a30c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0b0c`](#insn-00bb0b0c)

~~~json
{
  "source": "00bb0b0c",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0b14`](#insn-00bb0b14)

~~~json
{
  "source": "00bb0b14",
  "target": "002fa748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa748",
  "offset": 0,
  "size": 24,
  "datatype": "unicode32",
  "bytes": "410000007000000072000000690000006c00000000000000",
  "capture_start": "002fa748",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb0b18`](#insn-00bb0b18)

~~~json
{
  "source": "00bb0b18",
  "target": "010a30e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0b20`](#insn-00bb0b20)

~~~json
{
  "source": "00bb0b20",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0b24`](#insn-00bb0b24)

~~~json
{
  "source": "00bb0b24",
  "target": "010a30f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a30f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b28`](#insn-00bb0b28)

~~~json
{
  "source": "00bb0b28",
  "target": "00bb0b40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0b38`](#insn-00bb0b38)

~~~json
{
  "source": "00bb0b38",
  "target": "010a30f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a30f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b3c`](#insn-00bb0b3c)

~~~json
{
  "source": "00bb0b3c",
  "target": "00bb0b54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0b4c`](#insn-00bb0b4c)

~~~json
{
  "source": "00bb0b4c",
  "target": "010a3108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3104",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b50`](#insn-00bb0b50)

~~~json
{
  "source": "00bb0b50",
  "target": "010a3100",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a30fc",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b60`](#insn-00bb0b60)

~~~json
{
  "source": "00bb0b60",
  "target": "010a30fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a30fc",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b60`](#insn-00bb0b60)

~~~json
{
  "source": "00bb0b60",
  "target": "010a3104",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3104",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b68`](#insn-00bb0b68)

~~~json
{
  "source": "00bb0b68",
  "target": "010a3110",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3110",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b6c`](#insn-00bb0b6c)

~~~json
{
  "source": "00bb0b6c",
  "target": "00bb0b84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0b7c`](#insn-00bb0b7c)

~~~json
{
  "source": "00bb0b7c",
  "target": "010a3110",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3110",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b80`](#insn-00bb0b80)

~~~json
{
  "source": "00bb0b80",
  "target": "00bb0b98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0b90`](#insn-00bb0b90)

~~~json
{
  "source": "00bb0b90",
  "target": "010a3120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3120",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0b94`](#insn-00bb0b94)

~~~json
{
  "source": "00bb0b94",
  "target": "010a3118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ba0`](#insn-00bb0ba0)

~~~json
{
  "source": "00bb0ba0",
  "target": "010a3124",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3120",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ba4`](#insn-00bb0ba4)

~~~json
{
  "source": "00bb0ba4",
  "target": "002fa96c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ba8`](#insn-00bb0ba8)

~~~json
{
  "source": "00bb0ba8",
  "target": "010a3114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0bb0`](#insn-00bb0bb0)

~~~json
{
  "source": "00bb0bb0",
  "target": "010a3128",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3128",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0bb4`](#insn-00bb0bb4)

~~~json
{
  "source": "00bb0bb4",
  "target": "00bb0bcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0bc4`](#insn-00bb0bc4)

~~~json
{
  "source": "00bb0bc4",
  "target": "010a3128",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3128",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0bc8`](#insn-00bb0bc8)

~~~json
{
  "source": "00bb0bc8",
  "target": "00bb0be0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0bd8`](#insn-00bb0bd8)

~~~json
{
  "source": "00bb0bd8",
  "target": "010a3138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0bdc`](#insn-00bb0bdc)

~~~json
{
  "source": "00bb0bdc",
  "target": "010a3130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0bf0`](#insn-00bb0bf0)

~~~json
{
  "source": "00bb0bf0",
  "target": "002fa6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0bf8`](#insn-00bb0bf8)

~~~json
{
  "source": "00bb0bf8",
  "target": "002fa660",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa660",
  "offset": 0,
  "size": 28,
  "datatype": "unicode32",
  "bytes": "41000000750000006700000075000000730000007400000000000000",
  "capture_start": "002fa660",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb0bfc`](#insn-00bb0bfc)

~~~json
{
  "source": "00bb0bfc",
  "target": "010a3140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c04`](#insn-00bb0c04)

~~~json
{
  "source": "00bb0c04",
  "target": "010a312c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c0c`](#insn-00bb0c0c)

~~~json
{
  "source": "00bb0c0c",
  "target": "010a313c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3138",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0c10`](#insn-00bb0c10)

~~~json
{
  "source": "00bb0c10",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0c18`](#insn-00bb0c18)

~~~json
{
  "source": "00bb0c18",
  "target": "002fa6fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa6fc",
  "offset": 0,
  "size": 40,
  "datatype": "unicode32",
  "bytes": "53000000650000007000000074000000650000006d0000006200000065000000",
  "capture_start": "002fa6fc",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb0c1c`](#insn-00bb0c1c)

~~~json
{
  "source": "00bb0c1c",
  "target": "010a3158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c24`](#insn-00bb0c24)

~~~json
{
  "source": "00bb0c24",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0c2c`](#insn-00bb0c2c)

~~~json
{
  "source": "00bb0c2c",
  "target": "002fa8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa8a0",
  "offset": 0,
  "size": 32,
  "datatype": "unicode32",
  "bytes": "4f00000063000000740000006f00000062000000650000007200000000000000",
  "capture_start": "002fa8a0",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb0c30`](#insn-00bb0c30)

~~~json
{
  "source": "00bb0c30",
  "target": "010a3170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c38`](#insn-00bb0c38)

~~~json
{
  "source": "00bb0c38",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0c40`](#insn-00bb0c40)

~~~json
{
  "source": "00bb0c40",
  "target": "002fa7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa7a0",
  "offset": 0,
  "size": 36,
  "datatype": "unicode32",
  "bytes": "4e0000006f00000076000000650000006d000000620000006500000072000000",
  "capture_start": "002fa7a0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb0c44`](#insn-00bb0c44)

~~~json
{
  "source": "00bb0c44",
  "target": "010a3188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c4c`](#insn-00bb0c4c)

~~~json
{
  "source": "00bb0c4c",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0c54`](#insn-00bb0c54)

~~~json
{
  "source": "00bb0c54",
  "target": "002fa724",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fa724",
  "offset": 0,
  "size": 36,
  "datatype": "unicode32",
  "bytes": "440000006500000063000000650000006d000000620000006500000072000000",
  "capture_start": "002fa724",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb0c58`](#insn-00bb0c58)

~~~json
{
  "source": "00bb0c58",
  "target": "010a31a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c60`](#insn-00bb0c60)

~~~json
{
  "source": "00bb0c60",
  "target": "00b76424",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0c64`](#insn-00bb0c64)

~~~json
{
  "source": "00bb0c64",
  "target": "010a31b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0c68`](#insn-00bb0c68)

~~~json
{
  "source": "00bb0c68",
  "target": "00bb0c7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c74`](#insn-00bb0c74)

~~~json
{
  "source": "00bb0c74",
  "target": "010a31b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0c78`](#insn-00bb0c78)

~~~json
{
  "source": "00bb0c78",
  "target": "00bb0c90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0c88`](#insn-00bb0c88)

~~~json
{
  "source": "00bb0c88",
  "target": "010a31c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31c4",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0c8c`](#insn-00bb0c8c)

~~~json
{
  "source": "00bb0c8c",
  "target": "010a31c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31bc",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0c9c`](#insn-00bb0c9c)

~~~json
{
  "source": "00bb0c9c",
  "target": "010a31bc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31bc",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0c9c`](#insn-00bb0c9c)

~~~json
{
  "source": "00bb0c9c",
  "target": "010a31c4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31c4",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ca4`](#insn-00bb0ca4)

~~~json
{
  "source": "00bb0ca4",
  "target": "010a31d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ca8`](#insn-00bb0ca8)

~~~json
{
  "source": "00bb0ca8",
  "target": "00bb0cc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0cb8`](#insn-00bb0cb8)

~~~json
{
  "source": "00bb0cb8",
  "target": "010a31d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0cbc`](#insn-00bb0cbc)

~~~json
{
  "source": "00bb0cbc",
  "target": "00bb0cd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ccc`](#insn-00bb0ccc)

~~~json
{
  "source": "00bb0ccc",
  "target": "010a31e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31dc",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0cd0`](#insn-00bb0cd0)

~~~json
{
  "source": "00bb0cd0",
  "target": "010a31d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31d4",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ce0`](#insn-00bb0ce0)

~~~json
{
  "source": "00bb0ce0",
  "target": "010a31d4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31d4",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ce0`](#insn-00bb0ce0)

~~~json
{
  "source": "00bb0ce0",
  "target": "010a31dc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31dc",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ce8`](#insn-00bb0ce8)

~~~json
{
  "source": "00bb0ce8",
  "target": "010a31e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0cec`](#insn-00bb0cec)

~~~json
{
  "source": "00bb0cec",
  "target": "00bb0d04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0cfc`](#insn-00bb0cfc)

~~~json
{
  "source": "00bb0cfc",
  "target": "010a31e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d00`](#insn-00bb0d00)

~~~json
{
  "source": "00bb0d00",
  "target": "00bb0d18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0d10`](#insn-00bb0d10)

~~~json
{
  "source": "00bb0d10",
  "target": "010a31f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31f4",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d14`](#insn-00bb0d14)

~~~json
{
  "source": "00bb0d14",
  "target": "010a31f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31ec",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d24`](#insn-00bb0d24)

~~~json
{
  "source": "00bb0d24",
  "target": "010a31ec",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31ec",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d24`](#insn-00bb0d24)

~~~json
{
  "source": "00bb0d24",
  "target": "010a31f4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a31f4",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d2c`](#insn-00bb0d2c)

~~~json
{
  "source": "00bb0d2c",
  "target": "010a3200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3200",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d30`](#insn-00bb0d30)

~~~json
{
  "source": "00bb0d30",
  "target": "00bb0d48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0d40`](#insn-00bb0d40)

~~~json
{
  "source": "00bb0d40",
  "target": "010a3200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3200",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d44`](#insn-00bb0d44)

~~~json
{
  "source": "00bb0d44",
  "target": "00bb0d5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0d54`](#insn-00bb0d54)

~~~json
{
  "source": "00bb0d54",
  "target": "010a3210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a320c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d58`](#insn-00bb0d58)

~~~json
{
  "source": "00bb0d58",
  "target": "010a3208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3204",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d68`](#insn-00bb0d68)

~~~json
{
  "source": "00bb0d68",
  "target": "010a3204",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3204",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d68`](#insn-00bb0d68)

~~~json
{
  "source": "00bb0d68",
  "target": "010a320c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a320c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d70`](#insn-00bb0d70)

~~~json
{
  "source": "00bb0d70",
  "target": "010a3218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3218",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d74`](#insn-00bb0d74)

~~~json
{
  "source": "00bb0d74",
  "target": "00bb0d8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0d84`](#insn-00bb0d84)

~~~json
{
  "source": "00bb0d84",
  "target": "010a3218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3218",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d88`](#insn-00bb0d88)

~~~json
{
  "source": "00bb0d88",
  "target": "00bb0da0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0d98`](#insn-00bb0d98)

~~~json
{
  "source": "00bb0d98",
  "target": "010a3228",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3224",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0d9c`](#insn-00bb0d9c)

~~~json
{
  "source": "00bb0d9c",
  "target": "010a3220",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a321c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0dac`](#insn-00bb0dac)

~~~json
{
  "source": "00bb0dac",
  "target": "010a321c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a321c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0dac`](#insn-00bb0dac)

~~~json
{
  "source": "00bb0dac",
  "target": "010a3224",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3224",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0db4`](#insn-00bb0db4)

~~~json
{
  "source": "00bb0db4",
  "target": "010a3230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3230",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0db8`](#insn-00bb0db8)

~~~json
{
  "source": "00bb0db8",
  "target": "00bb0dd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0dc8`](#insn-00bb0dc8)

~~~json
{
  "source": "00bb0dc8",
  "target": "010a3230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3230",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0dcc`](#insn-00bb0dcc)

~~~json
{
  "source": "00bb0dcc",
  "target": "00bb0de4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ddc`](#insn-00bb0ddc)

~~~json
{
  "source": "00bb0ddc",
  "target": "010a3240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a323c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0de0`](#insn-00bb0de0)

~~~json
{
  "source": "00bb0de0",
  "target": "010a3238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3234",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0df0`](#insn-00bb0df0)

~~~json
{
  "source": "00bb0df0",
  "target": "010a3234",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3234",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0df0`](#insn-00bb0df0)

~~~json
{
  "source": "00bb0df0",
  "target": "010a323c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a323c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0df8`](#insn-00bb0df8)

~~~json
{
  "source": "00bb0df8",
  "target": "010a3248",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3248",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0dfc`](#insn-00bb0dfc)

~~~json
{
  "source": "00bb0dfc",
  "target": "00bb0e14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0e0c`](#insn-00bb0e0c)

~~~json
{
  "source": "00bb0e0c",
  "target": "010a3248",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3248",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e10`](#insn-00bb0e10)

~~~json
{
  "source": "00bb0e10",
  "target": "00bb0e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0e20`](#insn-00bb0e20)

~~~json
{
  "source": "00bb0e20",
  "target": "010a3258",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3254",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e24`](#insn-00bb0e24)

~~~json
{
  "source": "00bb0e24",
  "target": "010a3250",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a324c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e34`](#insn-00bb0e34)

~~~json
{
  "source": "00bb0e34",
  "target": "010a324c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a324c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e34`](#insn-00bb0e34)

~~~json
{
  "source": "00bb0e34",
  "target": "010a3254",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3254",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e3c`](#insn-00bb0e3c)

~~~json
{
  "source": "00bb0e3c",
  "target": "010a3260",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3260",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e40`](#insn-00bb0e40)

~~~json
{
  "source": "00bb0e40",
  "target": "00bb0e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0e50`](#insn-00bb0e50)

~~~json
{
  "source": "00bb0e50",
  "target": "010a3260",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3260",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e54`](#insn-00bb0e54)

~~~json
{
  "source": "00bb0e54",
  "target": "00bb0e6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0e64`](#insn-00bb0e64)

~~~json
{
  "source": "00bb0e64",
  "target": "010a3270",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a326c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e68`](#insn-00bb0e68)

~~~json
{
  "source": "00bb0e68",
  "target": "010a3268",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3264",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e78`](#insn-00bb0e78)

~~~json
{
  "source": "00bb0e78",
  "target": "010a3264",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3264",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e78`](#insn-00bb0e78)

~~~json
{
  "source": "00bb0e78",
  "target": "010a326c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a326c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e80`](#insn-00bb0e80)

~~~json
{
  "source": "00bb0e80",
  "target": "010a3278",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3278",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e84`](#insn-00bb0e84)

~~~json
{
  "source": "00bb0e84",
  "target": "00bb0e9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0e94`](#insn-00bb0e94)

~~~json
{
  "source": "00bb0e94",
  "target": "010a3278",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3278",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0e98`](#insn-00bb0e98)

~~~json
{
  "source": "00bb0e98",
  "target": "00bb0eb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ea8`](#insn-00bb0ea8)

~~~json
{
  "source": "00bb0ea8",
  "target": "010a3288",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3284",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0eac`](#insn-00bb0eac)

~~~json
{
  "source": "00bb0eac",
  "target": "010a3280",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a327c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ebc`](#insn-00bb0ebc)

~~~json
{
  "source": "00bb0ebc",
  "target": "010a327c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a327c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ebc`](#insn-00bb0ebc)

~~~json
{
  "source": "00bb0ebc",
  "target": "010a3284",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3284",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ec4`](#insn-00bb0ec4)

~~~json
{
  "source": "00bb0ec4",
  "target": "010a3290",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3290",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ec8`](#insn-00bb0ec8)

~~~json
{
  "source": "00bb0ec8",
  "target": "00bb0ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0ed8`](#insn-00bb0ed8)

~~~json
{
  "source": "00bb0ed8",
  "target": "010a3290",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3290",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0edc`](#insn-00bb0edc)

~~~json
{
  "source": "00bb0edc",
  "target": "00bb0ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0eec`](#insn-00bb0eec)

~~~json
{
  "source": "00bb0eec",
  "target": "010a32a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a329c",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0ef0`](#insn-00bb0ef0)

~~~json
{
  "source": "00bb0ef0",
  "target": "010a3298",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3294",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f00`](#insn-00bb0f00)

~~~json
{
  "source": "00bb0f00",
  "target": "010a3294",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3294",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f00`](#insn-00bb0f00)

~~~json
{
  "source": "00bb0f00",
  "target": "010a329c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a329c",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f08`](#insn-00bb0f08)

~~~json
{
  "source": "00bb0f08",
  "target": "010a32a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32a8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f0c`](#insn-00bb0f0c)

~~~json
{
  "source": "00bb0f0c",
  "target": "00bb0f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0f1c`](#insn-00bb0f1c)

~~~json
{
  "source": "00bb0f1c",
  "target": "010a32a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32a8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f20`](#insn-00bb0f20)

~~~json
{
  "source": "00bb0f20",
  "target": "00bb0f38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0f30`](#insn-00bb0f30)

~~~json
{
  "source": "00bb0f30",
  "target": "010a32b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32b4",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f34`](#insn-00bb0f34)

~~~json
{
  "source": "00bb0f34",
  "target": "010a32b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32ac",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f44`](#insn-00bb0f44)

~~~json
{
  "source": "00bb0f44",
  "target": "010a32ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32ac",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f44`](#insn-00bb0f44)

~~~json
{
  "source": "00bb0f44",
  "target": "010a32b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32b4",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f4c`](#insn-00bb0f4c)

~~~json
{
  "source": "00bb0f4c",
  "target": "010a32c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f50`](#insn-00bb0f50)

~~~json
{
  "source": "00bb0f50",
  "target": "00bb0f68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0f60`](#insn-00bb0f60)

~~~json
{
  "source": "00bb0f60",
  "target": "010a32c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f64`](#insn-00bb0f64)

~~~json
{
  "source": "00bb0f64",
  "target": "00bb0f7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0f74`](#insn-00bb0f74)

~~~json
{
  "source": "00bb0f74",
  "target": "010a32d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32cc",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f78`](#insn-00bb0f78)

~~~json
{
  "source": "00bb0f78",
  "target": "010a32c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32c4",
  "offset": 4,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f88`](#insn-00bb0f88)

~~~json
{
  "source": "00bb0f88",
  "target": "010a32c4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32c4",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f88`](#insn-00bb0f88)

~~~json
{
  "source": "00bb0f88",
  "target": "010a32cc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32cc",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0f8c`](#insn-00bb0f8c)

~~~json
{
  "source": "00bb0f8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0f90`](#insn-00bb0f90)

~~~json
{
  "source": "00bb0f90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0fa0`](#insn-00bb0fa0)

~~~json
{
  "source": "00bb0fa0",
  "target": "010a32d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0fa4`](#insn-00bb0fa4)

~~~json
{
  "source": "00bb0fa4",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0fa8`](#insn-00bb0fa8)

~~~json
{
  "source": "00bb0fa8",
  "target": "00bb0acc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0fb0`](#insn-00bb0fb0)

~~~json
{
  "source": "00bb0fb0",
  "target": "00bb8f54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0fb8`](#insn-00bb0fb8)

~~~json
{
  "source": "00bb0fb8",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb0fc0`](#insn-00bb0fc0)

~~~json
{
  "source": "00bb0fc0",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0fc8`](#insn-00bb0fc8)

~~~json
{
  "source": "00bb0fc8",
  "target": "010a32d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a32d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0fcc`](#insn-00bb0fcc)

~~~json
{
  "source": "00bb0fcc",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0fd0`](#insn-00bb0fd0)

~~~json
{
  "source": "00bb0fd0",
  "target": "00bb0acc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
