# 00bafc6c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bafc28`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-c69cca3e558ee268634d045f2df800c8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2c6b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-1e030a87c07d628587015c1bb6259987)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafc6c",
  "name": "FUN_00bafc6c",
  "size": 1080,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c3a17e7702b4dc0f078a2c2f0e9a42b872a34854a4ae5799a77161d405a2dd8",
  "source_text_sha256": "7c3a17e7702b4dc0f078a2c2f0e9a42b872a34854a4ae5799a77161d405a2dd8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafc6c",
        "00bb00a3"
      ]
    ],
    "bytes_sha256": "61ad7ba4403f65b08e6c651eaa47f5dc904e5381b9979f9a7b946e7a6374eb4d",
    "instruction_count": 270,
    "instruction_bytes": 1080,
    "body_bytes": 1080,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bafc00](../00baf/00bafc00.md)

## 呼び出し先

- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)

## 関連文字列（未確認候補）

~~~text
"Wednesday"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3745 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00bafc6c(void)

{
  undefined8 uVar1;
  int iVar2;
  char *pcVar3;
  undefined8 *puVar4;
  undefined4 *puVar5;
  
  if (((DAT_010a2df0 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_010a2df0), iVar2 != 0)) {
                    /* try { // try from 00bb0080 to 00cb0087 has its CatchHandler @ 00bb0df4 */
    __cxa_atexit(FUN_00bb8d30,0,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_010a2df0);
  }
  if ((DAT_010a2ca0 & 1) == 0) {
    DAT_010a2ca0 = 0xc;
    puVar5 = &DAT_010a2ca1;
  }
  else {
    DAT_010a2ca8 = 6;
    puVar5 = DAT_010a2cb0;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e7553;
  if ((DAT_010a2cb8 & 1) == 0) {
    DAT_010a2cb8 = 0xc;
    puVar5 = &DAT_010a2cb9;
  }
  else {
    DAT_010a2cc0 = 6;
    puVar5 = DAT_010a2cc8;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e6f4d;
  if ((DAT_010a2cd0 & 1) == 0) {
    DAT_010a2cd0 = 0xe;
    puVar5 = &DAT_010a2cd1;
  }
  else {
    DAT_010a2cd8 = 7;
    puVar5 = DAT_010a2ce0;
  }
  *(undefined1 *)((long)puVar5 + 7) = 0;
  *(undefined4 *)((long)puVar5 + 3) = 0x79616473;
  *puVar5 = 0x73657554;
  uVar1 = s_Wednesday_002a8090._0_8_;
  if ((DAT_010a2ce8 & 1) == 0) {
                    /* try { // try from 00bafd84 to 00cafdd3 has its CatchHandler @ 00bb0e00 */
    DAT_010a2ce8 = 0x12;
    pcVar3 = (char *)&DAT_010a2ce9;
  }
  else {
    ram0x010a2cf0 = 9;
    pcVar3 = DAT_010a2cf8;
  }
  pcVar3[8] = 'y';
  pcVar3[9] = '\0';
  *(undefined8 *)pcVar3 = uVar1;
  if ((DAT_010a2d00 & 1) == 0) {
    DAT_010a2d00 = 0x10;
    puVar4 = &DAT_010a2d01;
  }
  else {
    ram0x010a2d08 = 8;
    puVar4 = DAT_010a2d10;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7961647372756854;
  if ((DAT_010a2d18 & 1) == 0) {
    DAT_010a2d18 = 0xc;
    puVar5 = &DAT_010a2d19;
  }
  else {
    DAT_010a2d20 = 6;
    puVar5 = DAT_010a2d28;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
                    /* try { // try from 00bafe50 to 00cafff7 has its CatchHandler @ 00bb0e38 */
  *puVar5 = 0x64697246;
  if ((DAT_010a2d30 & 1) == 0) {
    DAT_010a2d30 = 0x10;
    puVar4 = &DAT_010a2d31;
  }
  else {
    ram0x010a2d38 = 8;
    puVar4 = DAT_010a2d40;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7961647275746153;
  if ((DAT_010a2d48 & 1) == 0) {
    DAT_010a2d48 = 6;
    puVar5 = &DAT_010a2d49;
  }
  else {
    DAT_010a2d50 = 3;
    puVar5 = DAT_010a2d58;
  }
  *puVar5 = 0x6e7553;
  if ((DAT_010a2d60 & 1) == 0) {
    DAT_010a2d60 = 6;
    puVar5 = &DAT_010a2d61;
  }
  else {
    DAT_010a2d68 = 3;
    puVar5 = DAT_010a2d70;
  }
  *puVar5 = 0x6e6f4d;
  if ((DAT_010a2d78 & 1) == 0) {
    DAT_010a2d78 = 6;
    puVar5 = &DAT_010a2d79;
  }
  else {
    DAT_010a2d80 = 3;
    puVar5 = DAT_010a2d88;
  }
  *puVar5 = 0x657554;
  if ((DAT_010a2d90 & 1) == 0) {
    DAT_010a2d90 = 6;
    puVar5 = &DAT_010a2d91;
  }
  else {
    DAT_010a2d98 = 3;
    puVar5 = DAT_010a2da0;
  }
  *puVar5 = 0x646557;
  if ((DAT_010a2da8 & 1) == 0) {
    DAT_010a2da8 = 6;
    puVar5 = &DAT_010a2da9;
  }
  else {
    DAT_010a2db0 = 3;
    puVar5 = DAT_010a2db8;
  }
  *puVar5 = 0x756854;
  if ((DAT_010a2dc0 & 1) == 0) {
                    /* try { // try from 00bafff8 to 00cb007f has its CatchHandler @ 00bafb60 */
    DAT_010a2dc0 = 6;
    puVar5 = &DAT_010a2dc1;
  }
  else {
    DAT_010a2dc8 = 3;
    puVar5 = DAT_010a2dd0;
  }
  *puVar5 = 0x697246;
  if ((DAT_010a2dd8 & 1) == 0) {
    DAT_010a2dd8 = 6;
    puVar5 = &DAT_010a2dd9;
  }
  else {
    DAT_010a2de0 = 3;
    puVar5 = DAT_010a2de8;
  }
  *puVar5 = 0x746153;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafc6c"></a> `00bafc6c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bafc70"></a> `00bafc70` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bafc74"></a> `00bafc74` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bafc78"></a> `00bafc78` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc7c"></a> `00bafc7c` | `08 c1 37 91` | add x8,x8,#0xdf0 | `FALL_THROUGH`
<a id="insn-00bafc80"></a> `00bafc80` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bafc84"></a> `00bafc84` | `48 1f 00 36` | tbz w8,#0x0,0x00bb006c | `CONDITIONAL_JUMP`
<a id="insn-00bafc88"></a> `00bafc88` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc8c"></a> `00bafc8c` | `08 81 72 39` | ldrb w8,[x8, #0xca0] | `FALL_THROUGH`
<a id="insn-00bafc90"></a> `00bafc90` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafca8 | `CONDITIONAL_JUMP`
<a id="insn-00bafc94"></a> `00bafc94` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafc98"></a> `00bafc98` | `08 81 32 91` | add x8,x8,#0xca0 | `FALL_THROUGH`
<a id="insn-00bafc9c"></a> `00bafc9c` | `89 01 80 52` | mov w9,#0xc | `FALL_THROUGH`
<a id="insn-00bafca0"></a> `00bafca0` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafca4"></a> `00bafca4` | `06 00 00 14` | b 0x00bafcbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bafca8"></a> `00bafca8` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafcac"></a> `00bafcac` | `29 a1 32 91` | add x9,x9,#0xca8 | `FALL_THROUGH`
<a id="insn-00bafcb0"></a> `00bafcb0` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00bafcb4"></a> `00bafcb4` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafcb8"></a> `00bafcb8` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafcbc"></a> `00bafcbc` | `6a aa 8e 52` | mov w10,#0x7553 | `FALL_THROUGH`
<a id="insn-00bafcc0"></a> `00bafcc0` | `29 2c 8f 52` | mov w9,#0x7961 | `FALL_THROUGH`
<a id="insn-00bafcc4"></a> `00bafcc4` | `1f 19 00 39` | strb wzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bafcc8"></a> `00bafcc8` | `ca 8d ac 72` | movk w10,#0x646e, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafccc"></a> `00bafccc` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bafcd0"></a> `00bafcd0` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafcd4"></a> `00bafcd4` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bafcd8"></a> `00bafcd8` | `28 e1 72 39` | ldrb w8,[x9, #0xcb8] | `FALL_THROUGH`
<a id="insn-00bafcdc"></a> `00bafcdc` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafcf4 | `CONDITIONAL_JUMP`
<a id="insn-00bafce0"></a> `00bafce0` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafce4"></a> `00bafce4` | `08 e1 32 91` | add x8,x8,#0xcb8 | `FALL_THROUGH`
<a id="insn-00bafce8"></a> `00bafce8` | `89 01 80 52` | mov w9,#0xc | `FALL_THROUGH`
<a id="insn-00bafcec"></a> `00bafcec` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafcf0"></a> `00bafcf0` | `06 00 00 14` | b 0x00bafd08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafcf4"></a> `00bafcf4` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafcf8"></a> `00bafcf8` | `29 01 33 91` | add x9,x9,#0xcc0 | `FALL_THROUGH`
<a id="insn-00bafcfc"></a> `00bafcfc` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00bafd00"></a> `00bafd00` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafd04"></a> `00bafd04` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafd08"></a> `00bafd08` | `aa e9 8d 52` | mov w10,#0x6f4d | `FALL_THROUGH`
<a id="insn-00bafd0c"></a> `00bafd0c` | `29 2c 8f 52` | mov w9,#0x7961 | `FALL_THROUGH`
<a id="insn-00bafd10"></a> `00bafd10` | `1f 19 00 39` | strb wzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bafd14"></a> `00bafd14` | `ca 8d ac 72` | movk w10,#0x646e, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafd18"></a> `00bafd18` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bafd1c"></a> `00bafd1c` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafd20"></a> `00bafd20` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bafd24"></a> `00bafd24` | `28 41 73 39` | ldrb w8,[x9, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bafd28"></a> `00bafd28` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafd40 | `CONDITIONAL_JUMP`
<a id="insn-00bafd2c"></a> `00bafd2c` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafd30"></a> `00bafd30` | `08 41 33 91` | add x8,x8,#0xcd0 | `FALL_THROUGH`
<a id="insn-00bafd34"></a> `00bafd34` | `c9 01 80 52` | mov w9,#0xe | `FALL_THROUGH`
<a id="insn-00bafd38"></a> `00bafd38` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafd3c"></a> `00bafd3c` | `06 00 00 14` | b 0x00bafd54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafd40"></a> `00bafd40` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafd44"></a> `00bafd44` | `29 61 33 91` | add x9,x9,#0xcd8 | `FALL_THROUGH`
<a id="insn-00bafd48"></a> `00bafd48` | `ea 00 80 52` | mov w10,#0x7 | `FALL_THROUGH`
<a id="insn-00bafd4c"></a> `00bafd4c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafd50"></a> `00bafd50` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafd54"></a> `00bafd54` | `69 8e 8c 52` | mov w9,#0x6473 | `FALL_THROUGH`
<a id="insn-00bafd58"></a> `00bafd58` | `8a aa 8e 52` | mov w10,#0x7554 | `FALL_THROUGH`
<a id="insn-00bafd5c"></a> `00bafd5c` | `1f 1d 00 39` | strb wzr,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00bafd60"></a> `00bafd60` | `29 2c af 72` | movk w9,#0x7961, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafd64"></a> `00bafd64` | `aa 6c ae 72` | movk w10,#0x7365, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafd68"></a> `00bafd68` | `09 31 00 b8` | stur w9,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bafd6c"></a> `00bafd6c` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafd70"></a> `00bafd70` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bafd74"></a> `00bafd74` | `28 a1 73 39` | ldrb w8,[x9, #0xce8] | `FALL_THROUGH`
<a id="insn-00bafd78"></a> `00bafd78` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafd90 | `CONDITIONAL_JUMP`
<a id="insn-00bafd7c"></a> `00bafd7c` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafd80"></a> `00bafd80` | `08 a1 33 91` | add x8,x8,#0xce8 | `FALL_THROUGH`
<a id="insn-00bafd84"></a> `00bafd84` | `49 02 80 52` | mov w9,#0x12 | `FALL_THROUGH`
<a id="insn-00bafd88"></a> `00bafd88` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafd8c"></a> `00bafd8c` | `06 00 00 14` | b 0x00bafda4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafd90"></a> `00bafd90` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafd94"></a> `00bafd94` | `29 c1 33 91` | add x9,x9,#0xcf0 | `FALL_THROUGH`
<a id="insn-00bafd98"></a> `00bafd98` | `2a 01 80 52` | mov w10,#0x9 | `FALL_THROUGH`
<a id="insn-00bafd9c"></a> `00bafd9c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafda0"></a> `00bafda0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafda4"></a> `00bafda4` | `ca b7 ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bafda8"></a> `00bafda8` | `4a 41 02 91` | add x10,x10,#0x90 | `FALL_THROUGH`
<a id="insn-00bafdac"></a> `00bafdac` | `29 0f 80 52` | mov w9,#0x79 | `FALL_THROUGH`
<a id="insn-00bafdb0"></a> `00bafdb0` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00bafdb4"></a> `00bafdb4` | `09 11 00 79` | strh w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafdb8"></a> `00bafdb8` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bafdbc"></a> `00bafdbc` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafdc0"></a> `00bafdc0` | `08 01 74 39` | ldrb w8,[x8, #0xd00] | `FALL_THROUGH`
<a id="insn-00bafdc4"></a> `00bafdc4` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafddc | `CONDITIONAL_JUMP`
<a id="insn-00bafdc8"></a> `00bafdc8` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafdcc"></a> `00bafdcc` | `08 01 34 91` | add x8,x8,#0xd00 | `FALL_THROUGH`
<a id="insn-00bafdd0"></a> `00bafdd0` | `09 02 80 52` | mov w9,#0x10 | `FALL_THROUGH`
<a id="insn-00bafdd4"></a> `00bafdd4` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafdd8"></a> `00bafdd8` | `06 00 00 14` | b 0x00bafdf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafddc"></a> `00bafddc` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafde0"></a> `00bafde0` | `29 21 34 91` | add x9,x9,#0xd08 | `FALL_THROUGH`
<a id="insn-00bafde4"></a> `00bafde4` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00bafde8"></a> `00bafde8` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafdec"></a> `00bafdec` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafdf0"></a> `00bafdf0` | `89 0a 8d d2` | mov x9,#0x6854 | `FALL_THROUGH`
<a id="insn-00bafdf4"></a> `00bafdf4` | `1f 21 00 39` | strb wzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafdf8"></a> `00bafdf8` | `a9 4e ae f2` | movk x9,#0x7275, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafdfc"></a> `00bafdfc` | `69 8e cc f2` | movk x9,#0x6473, LSL #32 | `FALL_THROUGH`
<a id="insn-00bafe00"></a> `00bafe00` | `29 2c ef f2` | movk x9,#0x7961, LSL #48 | `FALL_THROUGH`
<a id="insn-00bafe04"></a> `00bafe04` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bafe08"></a> `00bafe08` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafe0c"></a> `00bafe0c` | `08 61 74 39` | ldrb w8,[x8, #0xd18] | `FALL_THROUGH`
<a id="insn-00bafe10"></a> `00bafe10` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafe28 | `CONDITIONAL_JUMP`
<a id="insn-00bafe14"></a> `00bafe14` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafe18"></a> `00bafe18` | `08 61 34 91` | add x8,x8,#0xd18 | `FALL_THROUGH`
<a id="insn-00bafe1c"></a> `00bafe1c` | `89 01 80 52` | mov w9,#0xc | `FALL_THROUGH`
<a id="insn-00bafe20"></a> `00bafe20` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafe24"></a> `00bafe24` | `06 00 00 14` | b 0x00bafe3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe28"></a> `00bafe28` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafe2c"></a> `00bafe2c` | `29 81 34 91` | add x9,x9,#0xd20 | `FALL_THROUGH`
<a id="insn-00bafe30"></a> `00bafe30` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00bafe34"></a> `00bafe34` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe38"></a> `00bafe38` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafe3c"></a> `00bafe3c` | `ca 48 8e 52` | mov w10,#0x7246 | `FALL_THROUGH`
<a id="insn-00bafe40"></a> `00bafe40` | `29 2c 8f 52` | mov w9,#0x7961 | `FALL_THROUGH`
<a id="insn-00bafe44"></a> `00bafe44` | `1f 19 00 39` | strb wzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bafe48"></a> `00bafe48` | `2a 8d ac 72` | movk w10,#0x6469, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafe4c"></a> `00bafe4c` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bafe50"></a> `00bafe50` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafe54"></a> `00bafe54` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bafe58"></a> `00bafe58` | `28 c1 74 39` | ldrb w8,[x9, #0xd30] | `FALL_THROUGH`
<a id="insn-00bafe5c"></a> `00bafe5c` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafe74 | `CONDITIONAL_JUMP`
<a id="insn-00bafe60"></a> `00bafe60` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafe64"></a> `00bafe64` | `08 c1 34 91` | add x8,x8,#0xd30 | `FALL_THROUGH`
<a id="insn-00bafe68"></a> `00bafe68` | `09 02 80 52` | mov w9,#0x10 | `FALL_THROUGH`
<a id="insn-00bafe6c"></a> `00bafe6c` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafe70"></a> `00bafe70` | `06 00 00 14` | b 0x00bafe88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe74"></a> `00bafe74` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafe78"></a> `00bafe78` | `29 e1 34 91` | add x9,x9,#0xd38 | `FALL_THROUGH`
<a id="insn-00bafe7c"></a> `00bafe7c` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00bafe80"></a> `00bafe80` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe84"></a> `00bafe84` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafe88"></a> `00bafe88` | `69 2a 8c d2` | mov x9,#0x6153 | `FALL_THROUGH`
<a id="insn-00bafe8c"></a> `00bafe8c` | `1f 21 00 39` | strb wzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe90"></a> `00bafe90` | `89 ae ae f2` | movk x9,#0x7574, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafe94"></a> `00bafe94` | `49 8e cc f2` | movk x9,#0x6472, LSL #32 | `FALL_THROUGH`
<a id="insn-00bafe98"></a> `00bafe98` | `29 2c ef f2` | movk x9,#0x7961, LSL #48 | `FALL_THROUGH`
<a id="insn-00bafe9c"></a> `00bafe9c` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bafea0"></a> `00bafea0` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafea4"></a> `00bafea4` | `08 21 75 39` | ldrb w8,[x8, #0xd48] | `FALL_THROUGH`
<a id="insn-00bafea8"></a> `00bafea8` | `c8 00 00 37` | tbnz w8,#0x0,0x00bafec0 | `CONDITIONAL_JUMP`
<a id="insn-00bafeac"></a> `00bafeac` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafeb0"></a> `00bafeb0` | `08 21 35 91` | add x8,x8,#0xd48 | `FALL_THROUGH`
<a id="insn-00bafeb4"></a> `00bafeb4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bafeb8"></a> `00bafeb8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafebc"></a> `00bafebc` | `06 00 00 14` | b 0x00bafed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafec0"></a> `00bafec0` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafec4"></a> `00bafec4` | `29 41 35 91` | add x9,x9,#0xd50 | `FALL_THROUGH`
<a id="insn-00bafec8"></a> `00bafec8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bafecc"></a> `00bafecc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bafed0"></a> `00bafed0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bafed4"></a> `00bafed4` | `69 aa 8e 52` | mov w9,#0x7553 | `FALL_THROUGH`
<a id="insn-00bafed8"></a> `00bafed8` | `c9 0d a0 72` | movk w9,#0x6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00bafedc"></a> `00bafedc` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00bafee0"></a> `00bafee0` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafee4"></a> `00bafee4` | `08 81 75 39` | ldrb w8,[x8, #0xd60] | `FALL_THROUGH`
<a id="insn-00bafee8"></a> `00bafee8` | `c8 00 00 37` | tbnz w8,#0x0,0x00baff00 | `CONDITIONAL_JUMP`
<a id="insn-00bafeec"></a> `00bafeec` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafef0"></a> `00bafef0` | `08 81 35 91` | add x8,x8,#0xd60 | `FALL_THROUGH`
<a id="insn-00bafef4"></a> `00bafef4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bafef8"></a> `00bafef8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafefc"></a> `00bafefc` | `06 00 00 14` | b 0x00baff14 | `UNCONDITIONAL_JUMP`
<a id="insn-00baff00"></a> `00baff00` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff04"></a> `00baff04` | `29 a1 35 91` | add x9,x9,#0xd68 | `FALL_THROUGH`
<a id="insn-00baff08"></a> `00baff08` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00baff0c"></a> `00baff0c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00baff10"></a> `00baff10` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00baff14"></a> `00baff14` | `a9 e9 8d 52` | mov w9,#0x6f4d | `FALL_THROUGH`
<a id="insn-00baff18"></a> `00baff18` | `c9 0d a0 72` | movk w9,#0x6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00baff1c"></a> `00baff1c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00baff20"></a> `00baff20` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff24"></a> `00baff24` | `08 e1 75 39` | ldrb w8,[x8, #0xd78] | `FALL_THROUGH`
<a id="insn-00baff28"></a> `00baff28` | `c8 00 00 37` | tbnz w8,#0x0,0x00baff40 | `CONDITIONAL_JUMP`
<a id="insn-00baff2c"></a> `00baff2c` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff30"></a> `00baff30` | `08 e1 35 91` | add x8,x8,#0xd78 | `FALL_THROUGH`
<a id="insn-00baff34"></a> `00baff34` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00baff38"></a> `00baff38` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00baff3c"></a> `00baff3c` | `06 00 00 14` | b 0x00baff54 | `UNCONDITIONAL_JUMP`
<a id="insn-00baff40"></a> `00baff40` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff44"></a> `00baff44` | `29 01 36 91` | add x9,x9,#0xd80 | `FALL_THROUGH`
<a id="insn-00baff48"></a> `00baff48` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00baff4c"></a> `00baff4c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00baff50"></a> `00baff50` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00baff54"></a> `00baff54` | `89 aa 8e 52` | mov w9,#0x7554 | `FALL_THROUGH`
<a id="insn-00baff58"></a> `00baff58` | `a9 0c a0 72` | movk w9,#0x65, LSL #16 | `FALL_THROUGH`
<a id="insn-00baff5c"></a> `00baff5c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00baff60"></a> `00baff60` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff64"></a> `00baff64` | `08 41 76 39` | ldrb w8,[x8, #0xd90] | `FALL_THROUGH`
<a id="insn-00baff68"></a> `00baff68` | `c8 00 00 37` | tbnz w8,#0x0,0x00baff80 | `CONDITIONAL_JUMP`
<a id="insn-00baff6c"></a> `00baff6c` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff70"></a> `00baff70` | `08 41 36 91` | add x8,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-00baff74"></a> `00baff74` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00baff78"></a> `00baff78` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00baff7c"></a> `00baff7c` | `06 00 00 14` | b 0x00baff94 | `UNCONDITIONAL_JUMP`
<a id="insn-00baff80"></a> `00baff80` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baff84"></a> `00baff84` | `29 61 36 91` | add x9,x9,#0xd98 | `FALL_THROUGH`
<a id="insn-00baff88"></a> `00baff88` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00baff8c"></a> `00baff8c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00baff90"></a> `00baff90` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00baff94"></a> `00baff94` | `e9 aa 8c 52` | mov w9,#0x6557 | `FALL_THROUGH`
<a id="insn-00baff98"></a> `00baff98` | `89 0c a0 72` | movk w9,#0x64, LSL #16 | `FALL_THROUGH`
<a id="insn-00baff9c"></a> `00baff9c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00baffa0"></a> `00baffa0` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baffa4"></a> `00baffa4` | `08 a1 76 39` | ldrb w8,[x8, #0xda8] | `FALL_THROUGH`
<a id="insn-00baffa8"></a> `00baffa8` | `c8 00 00 37` | tbnz w8,#0x0,0x00baffc0 | `CONDITIONAL_JUMP`
<a id="insn-00baffac"></a> `00baffac` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baffb0"></a> `00baffb0` | `08 a1 36 91` | add x8,x8,#0xda8 | `FALL_THROUGH`
<a id="insn-00baffb4"></a> `00baffb4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00baffb8"></a> `00baffb8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00baffbc"></a> `00baffbc` | `06 00 00 14` | b 0x00baffd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baffc0"></a> `00baffc0` | `89 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baffc4"></a> `00baffc4` | `29 c1 36 91` | add x9,x9,#0xdb0 | `FALL_THROUGH`
<a id="insn-00baffc8"></a> `00baffc8` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00baffcc"></a> `00baffcc` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00baffd0"></a> `00baffd0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00baffd4"></a> `00baffd4` | `89 0a 8d 52` | mov w9,#0x6854 | `FALL_THROUGH`
<a id="insn-00baffd8"></a> `00baffd8` | `a9 0e a0 72` | movk w9,#0x75, LSL #16 | `FALL_THROUGH`
<a id="insn-00baffdc"></a> `00baffdc` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00baffe0"></a> `00baffe0` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00baffe4"></a> `00baffe4` | `08 01 77 39` | ldrb w8,[x8, #0xdc0] | `FALL_THROUGH`
<a id="insn-00baffe8"></a> `00baffe8` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0000 | `CONDITIONAL_JUMP`
<a id="insn-00baffec"></a> `00baffec` | `88 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bafff0"></a> `00bafff0` | `08 01 37 91` | add x8,x8,#0xdc0 | `FALL_THROUGH`
<a id="insn-00bafff4"></a> `00bafff4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bafff8"></a> `00bafff8` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafffc"></a> `00bafffc` | `06 00 00 14` | b 0x00bb0014 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0000"></a> `00bb0000` | `89 27 00 d0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb0004"></a> `00bb0004` | `29 21 37 91` | add x9,x9,#0xdc8 | `FALL_THROUGH`
<a id="insn-00bb0008"></a> `00bb0008` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb000c"></a> `00bb000c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0010"></a> `00bb0010` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0014"></a> `00bb0014` | `c9 48 8e 52` | mov w9,#0x7246 | `FALL_THROUGH`
<a id="insn-00bb0018"></a> `00bb0018` | `29 0d a0 72` | movk w9,#0x69, LSL #16 | `FALL_THROUGH`
<a id="insn-00bb001c"></a> `00bb001c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00bb0020"></a> `00bb0020` | `88 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb0024"></a> `00bb0024` | `08 61 77 39` | ldrb w8,[x8, #0xdd8] | `FALL_THROUGH`
<a id="insn-00bb0028"></a> `00bb0028` | `c8 00 00 37` | tbnz w8,#0x0,0x00bb0040 | `CONDITIONAL_JUMP`
<a id="insn-00bb002c"></a> `00bb002c` | `88 27 00 d0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb0030"></a> `00bb0030` | `08 61 37 91` | add x8,x8,#0xdd8 | `FALL_THROUGH`
<a id="insn-00bb0034"></a> `00bb0034` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00bb0038"></a> `00bb0038` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bb003c"></a> `00bb003c` | `06 00 00 14` | b 0x00bb0054 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0040"></a> `00bb0040` | `89 27 00 d0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb0044"></a> `00bb0044` | `29 81 37 91` | add x9,x9,#0xde0 | `FALL_THROUGH`
<a id="insn-00bb0048"></a> `00bb0048` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb004c"></a> `00bb004c` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0050"></a> `00bb0050` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bb0054"></a> `00bb0054` | `69 2a 8c 52` | mov w9,#0x6153 | `FALL_THROUGH`
<a id="insn-00bb0058"></a> `00bb0058` | `89 0e a0 72` | movk w9,#0x74, LSL #16 | `FALL_THROUGH`
<a id="insn-00bb005c"></a> `00bb005c` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00bb0060"></a> `00bb0060` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bb0064"></a> `00bb0064` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb0068"></a> `00bb0068` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb006c"></a> `00bb006c` | `80 27 00 d0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb0070"></a> `00bb0070` | `00 c0 37 91` | add x0,x0,#0xdf0 | `FALL_THROUGH`
<a id="insn-00bb0074"></a> `00bb0074` | `e3 ab 00 94` | bl 0x00bdb000 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0078"></a> `00bb0078` | `80 e0 ff 34` | cbz w0,0x00bafc88 | `CONDITIONAL_JUMP`
<a id="insn-00bb007c"></a> `00bb007c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bb0080"></a> `00bb0080` | `80 65 04 10` | adr x0,0xbb8d30 | `FALL_THROUGH`
<a id="insn-00bb0084"></a> `00bb0084` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bb0088"></a> `00bb0088` | `42 fa 1a 10` | adr x2,0xbe5fd0 | `FALL_THROUGH`
<a id="insn-00bb008c"></a> `00bb008c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bb0090"></a> `00bb0090` | `d4 ab 00 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0094"></a> `00bb0094` | `80 27 00 d0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb0098"></a> `00bb0098` | `00 c0 37 91` | add x0,x0,#0xdf0 | `FALL_THROUGH`
<a id="insn-00bb009c"></a> `00bb009c` | `e1 ab 00 94` | bl 0x00bdb020 | `UNCONDITIONAL_CALL`
<a id="insn-00bb00a0"></a> `00bb00a0` | `fa fe ff 17` | b 0x00bafc88 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bafc6c`](#insn-00bafc6c) 範囲 `[['00bafc6c', '00bafc87']]`
  - `CONDITIONAL_JUMP` [`00bafc84`](#insn-00bafc84) → [`00bb006c`](#insn-00bb006c)
  - `FALL_THROUGH` [`00bafc84`](#insn-00bafc84) → [`00bafc88`](#insn-00bafc88)
- ブロック [`00bafc88`](#insn-00bafc88) 範囲 `[['00bafc88', '00bafc93']]`
  - `CONDITIONAL_JUMP` [`00bafc90`](#insn-00bafc90) → [`00bafca8`](#insn-00bafca8)
  - `FALL_THROUGH` [`00bafc90`](#insn-00bafc90) → [`00bafc94`](#insn-00bafc94)
- ブロック [`00bafc94`](#insn-00bafc94) 範囲 `[['00bafc94', '00bafca7']]`
  - `UNCONDITIONAL_JUMP` [`00bafca4`](#insn-00bafca4) → [`00bafcbc`](#insn-00bafcbc)
- ブロック [`00bafca8`](#insn-00bafca8) 範囲 `[['00bafca8', '00bafcbb']]`
  - `FALL_THROUGH` [`00bafcb8`](#insn-00bafcb8) → [`00bafcbc`](#insn-00bafcbc)
- ブロック [`00bafcbc`](#insn-00bafcbc) 範囲 `[['00bafcbc', '00bafcdf']]`
  - `CONDITIONAL_JUMP` [`00bafcdc`](#insn-00bafcdc) → [`00bafcf4`](#insn-00bafcf4)
  - `FALL_THROUGH` [`00bafcdc`](#insn-00bafcdc) → [`00bafce0`](#insn-00bafce0)
- ブロック [`00bafce0`](#insn-00bafce0) 範囲 `[['00bafce0', '00bafcf3']]`
  - `UNCONDITIONAL_JUMP` [`00bafcf0`](#insn-00bafcf0) → [`00bafd08`](#insn-00bafd08)
- ブロック [`00bafcf4`](#insn-00bafcf4) 範囲 `[['00bafcf4', '00bafd07']]`
  - `FALL_THROUGH` [`00bafd04`](#insn-00bafd04) → [`00bafd08`](#insn-00bafd08)
- ブロック [`00bafd08`](#insn-00bafd08) 範囲 `[['00bafd08', '00bafd2b']]`
  - `CONDITIONAL_JUMP` [`00bafd28`](#insn-00bafd28) → [`00bafd40`](#insn-00bafd40)
  - `FALL_THROUGH` [`00bafd28`](#insn-00bafd28) → [`00bafd2c`](#insn-00bafd2c)
- ブロック [`00bafd2c`](#insn-00bafd2c) 範囲 `[['00bafd2c', '00bafd3f']]`
  - `UNCONDITIONAL_JUMP` [`00bafd3c`](#insn-00bafd3c) → [`00bafd54`](#insn-00bafd54)
- ブロック [`00bafd40`](#insn-00bafd40) 範囲 `[['00bafd40', '00bafd53']]`
  - `FALL_THROUGH` [`00bafd50`](#insn-00bafd50) → [`00bafd54`](#insn-00bafd54)
- ブロック [`00bafd54`](#insn-00bafd54) 範囲 `[['00bafd54', '00bafd7b']]`
  - `CONDITIONAL_JUMP` [`00bafd78`](#insn-00bafd78) → [`00bafd90`](#insn-00bafd90)
  - `FALL_THROUGH` [`00bafd78`](#insn-00bafd78) → [`00bafd7c`](#insn-00bafd7c)
- ブロック [`00bafd7c`](#insn-00bafd7c) 範囲 `[['00bafd7c', '00bafd83']]`
  - `FALL_THROUGH` [`00bafd80`](#insn-00bafd80) → [`00bafd84`](#insn-00bafd84)
- ブロック [`00bafd84`](#insn-00bafd84) 範囲 `[['00bafd84', '00bafd8f']]`
  - `UNCONDITIONAL_JUMP` [`00bafd8c`](#insn-00bafd8c) → [`00bafda4`](#insn-00bafda4)
- ブロック [`00bafd90`](#insn-00bafd90) 範囲 `[['00bafd90', '00bafda3']]`
  - `FALL_THROUGH` [`00bafda0`](#insn-00bafda0) → [`00bafda4`](#insn-00bafda4)
- ブロック [`00bafda4`](#insn-00bafda4) 範囲 `[['00bafda4', '00bafdc7']]`
  - `CONDITIONAL_JUMP` [`00bafdc4`](#insn-00bafdc4) → [`00bafddc`](#insn-00bafddc)
  - `FALL_THROUGH` [`00bafdc4`](#insn-00bafdc4) → [`00bafdc8`](#insn-00bafdc8)
- ブロック [`00bafdc8`](#insn-00bafdc8) 範囲 `[['00bafdc8', '00bafddb']]`
  - `UNCONDITIONAL_JUMP` [`00bafdd8`](#insn-00bafdd8) → [`00bafdf0`](#insn-00bafdf0)
- ブロック [`00bafddc`](#insn-00bafddc) 範囲 `[['00bafddc', '00bafdef']]`
  - `FALL_THROUGH` [`00bafdec`](#insn-00bafdec) → [`00bafdf0`](#insn-00bafdf0)
- ブロック [`00bafdf0`](#insn-00bafdf0) 範囲 `[['00bafdf0', '00bafe13']]`
  - `CONDITIONAL_JUMP` [`00bafe10`](#insn-00bafe10) → [`00bafe28`](#insn-00bafe28)
  - `FALL_THROUGH` [`00bafe10`](#insn-00bafe10) → [`00bafe14`](#insn-00bafe14)
- ブロック [`00bafe14`](#insn-00bafe14) 範囲 `[['00bafe14', '00bafe27']]`
  - `UNCONDITIONAL_JUMP` [`00bafe24`](#insn-00bafe24) → [`00bafe3c`](#insn-00bafe3c)
- ブロック [`00bafe28`](#insn-00bafe28) 範囲 `[['00bafe28', '00bafe3b']]`
  - `FALL_THROUGH` [`00bafe38`](#insn-00bafe38) → [`00bafe3c`](#insn-00bafe3c)
- ブロック [`00bafe3c`](#insn-00bafe3c) 範囲 `[['00bafe3c', '00bafe4f']]`
  - `FALL_THROUGH` [`00bafe4c`](#insn-00bafe4c) → [`00bafe50`](#insn-00bafe50)
- ブロック [`00bafe50`](#insn-00bafe50) 範囲 `[['00bafe50', '00bafe5f']]`
  - `CONDITIONAL_JUMP` [`00bafe5c`](#insn-00bafe5c) → [`00bafe74`](#insn-00bafe74)
  - `FALL_THROUGH` [`00bafe5c`](#insn-00bafe5c) → [`00bafe60`](#insn-00bafe60)
- ブロック [`00bafe60`](#insn-00bafe60) 範囲 `[['00bafe60', '00bafe73']]`
  - `UNCONDITIONAL_JUMP` [`00bafe70`](#insn-00bafe70) → [`00bafe88`](#insn-00bafe88)
- ブロック [`00bafe74`](#insn-00bafe74) 範囲 `[['00bafe74', '00bafe87']]`
  - `FALL_THROUGH` [`00bafe84`](#insn-00bafe84) → [`00bafe88`](#insn-00bafe88)
- ブロック [`00bafe88`](#insn-00bafe88) 範囲 `[['00bafe88', '00bafeab']]`
  - `CONDITIONAL_JUMP` [`00bafea8`](#insn-00bafea8) → [`00bafec0`](#insn-00bafec0)
  - `FALL_THROUGH` [`00bafea8`](#insn-00bafea8) → [`00bafeac`](#insn-00bafeac)
- ブロック [`00bafeac`](#insn-00bafeac) 範囲 `[['00bafeac', '00bafebf']]`
  - `UNCONDITIONAL_JUMP` [`00bafebc`](#insn-00bafebc) → [`00bafed4`](#insn-00bafed4)
- ブロック [`00bafec0`](#insn-00bafec0) 範囲 `[['00bafec0', '00bafed3']]`
  - `FALL_THROUGH` [`00bafed0`](#insn-00bafed0) → [`00bafed4`](#insn-00bafed4)
- ブロック [`00bafed4`](#insn-00bafed4) 範囲 `[['00bafed4', '00bafeeb']]`
  - `CONDITIONAL_JUMP` [`00bafee8`](#insn-00bafee8) → [`00baff00`](#insn-00baff00)
  - `FALL_THROUGH` [`00bafee8`](#insn-00bafee8) → [`00bafeec`](#insn-00bafeec)
- ブロック [`00bafeec`](#insn-00bafeec) 範囲 `[['00bafeec', '00bafeff']]`
  - `UNCONDITIONAL_JUMP` [`00bafefc`](#insn-00bafefc) → [`00baff14`](#insn-00baff14)
- ブロック [`00baff00`](#insn-00baff00) 範囲 `[['00baff00', '00baff13']]`
  - `FALL_THROUGH` [`00baff10`](#insn-00baff10) → [`00baff14`](#insn-00baff14)
- ブロック [`00baff14`](#insn-00baff14) 範囲 `[['00baff14', '00baff2b']]`
  - `CONDITIONAL_JUMP` [`00baff28`](#insn-00baff28) → [`00baff40`](#insn-00baff40)
  - `FALL_THROUGH` [`00baff28`](#insn-00baff28) → [`00baff2c`](#insn-00baff2c)
- ブロック [`00baff2c`](#insn-00baff2c) 範囲 `[['00baff2c', '00baff3f']]`
  - `UNCONDITIONAL_JUMP` [`00baff3c`](#insn-00baff3c) → [`00baff54`](#insn-00baff54)
- ブロック [`00baff40`](#insn-00baff40) 範囲 `[['00baff40', '00baff53']]`
  - `FALL_THROUGH` [`00baff50`](#insn-00baff50) → [`00baff54`](#insn-00baff54)
- ブロック [`00baff54`](#insn-00baff54) 範囲 `[['00baff54', '00baff6b']]`
  - `CONDITIONAL_JUMP` [`00baff68`](#insn-00baff68) → [`00baff80`](#insn-00baff80)
  - `FALL_THROUGH` [`00baff68`](#insn-00baff68) → [`00baff6c`](#insn-00baff6c)
- ブロック [`00baff6c`](#insn-00baff6c) 範囲 `[['00baff6c', '00baff7f']]`
  - `UNCONDITIONAL_JUMP` [`00baff7c`](#insn-00baff7c) → [`00baff94`](#insn-00baff94)
- ブロック [`00baff80`](#insn-00baff80) 範囲 `[['00baff80', '00baff93']]`
  - `FALL_THROUGH` [`00baff90`](#insn-00baff90) → [`00baff94`](#insn-00baff94)
- ブロック [`00baff94`](#insn-00baff94) 範囲 `[['00baff94', '00baffab']]`
  - `CONDITIONAL_JUMP` [`00baffa8`](#insn-00baffa8) → [`00baffc0`](#insn-00baffc0)
  - `FALL_THROUGH` [`00baffa8`](#insn-00baffa8) → [`00baffac`](#insn-00baffac)
- ブロック [`00baffac`](#insn-00baffac) 範囲 `[['00baffac', '00baffbf']]`
  - `UNCONDITIONAL_JUMP` [`00baffbc`](#insn-00baffbc) → [`00baffd4`](#insn-00baffd4)
- ブロック [`00baffc0`](#insn-00baffc0) 範囲 `[['00baffc0', '00baffd3']]`
  - `FALL_THROUGH` [`00baffd0`](#insn-00baffd0) → [`00baffd4`](#insn-00baffd4)
- ブロック [`00baffd4`](#insn-00baffd4) 範囲 `[['00baffd4', '00baffeb']]`
  - `CONDITIONAL_JUMP` [`00baffe8`](#insn-00baffe8) → [`00bb0000`](#insn-00bb0000)
  - `FALL_THROUGH` [`00baffe8`](#insn-00baffe8) → [`00baffec`](#insn-00baffec)
- ブロック [`00baffec`](#insn-00baffec) 範囲 `[['00baffec', '00bafff7']]`
  - `FALL_THROUGH` [`00bafff4`](#insn-00bafff4) → [`00bafff8`](#insn-00bafff8)
- ブロック [`00bafff8`](#insn-00bafff8) 範囲 `[['00bafff8', '00baffff']]`
  - `UNCONDITIONAL_JUMP` [`00bafffc`](#insn-00bafffc) → [`00bb0014`](#insn-00bb0014)
- ブロック [`00bb0000`](#insn-00bb0000) 範囲 `[['00bb0000', '00bb0013']]`
  - `FALL_THROUGH` [`00bb0010`](#insn-00bb0010) → [`00bb0014`](#insn-00bb0014)
- ブロック [`00bb0014`](#insn-00bb0014) 範囲 `[['00bb0014', '00bb002b']]`
  - `CONDITIONAL_JUMP` [`00bb0028`](#insn-00bb0028) → [`00bb0040`](#insn-00bb0040)
  - `FALL_THROUGH` [`00bb0028`](#insn-00bb0028) → [`00bb002c`](#insn-00bb002c)
- ブロック [`00bb002c`](#insn-00bb002c) 範囲 `[['00bb002c', '00bb003f']]`
  - `UNCONDITIONAL_JUMP` [`00bb003c`](#insn-00bb003c) → [`00bb0054`](#insn-00bb0054)
- ブロック [`00bb0040`](#insn-00bb0040) 範囲 `[['00bb0040', '00bb0053']]`
  - `FALL_THROUGH` [`00bb0050`](#insn-00bb0050) → [`00bb0054`](#insn-00bb0054)
- ブロック [`00bb0054`](#insn-00bb0054) 範囲 `[['00bb0054', '00bb006b']]`
- ブロック [`00bb006c`](#insn-00bb006c) 範囲 `[['00bb006c', '00bb007b']]`
  - `CONDITIONAL_JUMP` [`00bb0078`](#insn-00bb0078) → [`00bafc88`](#insn-00bafc88)
  - `FALL_THROUGH` [`00bb0078`](#insn-00bb0078) → [`00bb007c`](#insn-00bb007c)
- ブロック [`00bb007c`](#insn-00bb007c) 範囲 `[['00bb007c', '00bb007f']]`
  - `FALL_THROUGH` [`00bb007c`](#insn-00bb007c) → [`00bb0080`](#insn-00bb0080)
- ブロック [`00bb0080`](#insn-00bb0080) 範囲 `[['00bb0080', '00bb00a3']]`
  - `UNCONDITIONAL_JUMP` [`00bb00a0`](#insn-00bb00a0) → [`00bafc88`](#insn-00bafc88)

## 命令位置別の参照

- [`00bafc70`](#insn-00bafc70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc80`](#insn-00bafc80) → `010a2df0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafc84`](#insn-00bafc84) → [`00bb006c`](#insn-00bb006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc8c`](#insn-00bafc8c) → `010a2ca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafc90`](#insn-00bafc90) → [`00bafca8`](#insn-00bafca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafca0`](#insn-00bafca0) → `010a2ca0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafca4`](#insn-00bafca4) → [`00bafcbc`](#insn-00bafcbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcb4`](#insn-00bafcb4) → `010a2cb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafcb8`](#insn-00bafcb8) → `010a2ca8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafcc4`](#insn-00bafcc4) → `010a2ca7`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafccc`](#insn-00bafccc) → `010a2ca5`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00bafcd4`](#insn-00bafcd4) → `010a2ca1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bafcd8`](#insn-00bafcd8) → `010a2cb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafcdc`](#insn-00bafcdc) → [`00bafcf4`](#insn-00bafcf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcec`](#insn-00bafcec) → `010a2cb8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafcf0`](#insn-00bafcf0) → [`00bafd08`](#insn-00bafd08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd00`](#insn-00bafd00) → `010a2cc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafd04`](#insn-00bafd04) → `010a2cc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafd10`](#insn-00bafd10) → `010a2cbf`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafd18`](#insn-00bafd18) → `010a2cbd`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00bafd20`](#insn-00bafd20) → `010a2cb9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bafd24`](#insn-00bafd24) → `010a2cd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafd28`](#insn-00bafd28) → [`00bafd40`](#insn-00bafd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd38`](#insn-00bafd38) → `010a2cd0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafd3c`](#insn-00bafd3c) → [`00bafd54`](#insn-00bafd54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd4c`](#insn-00bafd4c) → `010a2ce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafd50`](#insn-00bafd50) → `010a2cd8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafd5c`](#insn-00bafd5c) → `010a2cd8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafd68`](#insn-00bafd68) → `010a2cd4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bafd70`](#insn-00bafd70) → `010a2cd1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bafd74`](#insn-00bafd74) → `010a2ce8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafd78`](#insn-00bafd78) → [`00bafd90`](#insn-00bafd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd88`](#insn-00bafd88) → `010a2ce8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafd8c`](#insn-00bafd8c) → [`00bafda4`](#insn-00bafda4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd9c`](#insn-00bafd9c) → `010a2cf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafda0`](#insn-00bafda0) → `010a2cf0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafdb0`](#insn-00bafdb0) → `002a8090`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bafdb4`](#insn-00bafdb4) → `010a2cf1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00bafdb8`](#insn-00bafdb8) → `010a2ce9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafdc0`](#insn-00bafdc0) → `010a2d00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafdc4`](#insn-00bafdc4) → [`00bafddc`](#insn-00bafddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdd4`](#insn-00bafdd4) → `010a2d00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafdd8`](#insn-00bafdd8) → [`00bafdf0`](#insn-00bafdf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafde8`](#insn-00bafde8) → `010a2d10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafdec`](#insn-00bafdec) → `010a2d08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafdf4`](#insn-00bafdf4) → `010a2d09`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe04`](#insn-00bafe04) → `010a2d01`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafe0c`](#insn-00bafe0c) → `010a2d18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe10`](#insn-00bafe10) → [`00bafe28`](#insn-00bafe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe20`](#insn-00bafe20) → `010a2d18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe24`](#insn-00bafe24) → [`00bafe3c`](#insn-00bafe3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe34`](#insn-00bafe34) → `010a2d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafe38`](#insn-00bafe38) → `010a2d20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafe44`](#insn-00bafe44) → `010a2d1f`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe4c`](#insn-00bafe4c) → `010a2d1d`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00bafe54`](#insn-00bafe54) → `010a2d19`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bafe58`](#insn-00bafe58) → `010a2d30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe5c`](#insn-00bafe5c) → [`00bafe74`](#insn-00bafe74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe6c`](#insn-00bafe6c) → `010a2d30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe70`](#insn-00bafe70) → [`00bafe88`](#insn-00bafe88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe80`](#insn-00bafe80) → `010a2d40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafe84`](#insn-00bafe84) → `010a2d38`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafe8c`](#insn-00bafe8c) → `010a2d39`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafe9c`](#insn-00bafe9c) → `010a2d31`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafea4`](#insn-00bafea4) → `010a2d48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafea8`](#insn-00bafea8) → [`00bafec0`](#insn-00bafec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafeb8`](#insn-00bafeb8) → `010a2d48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafebc`](#insn-00bafebc) → [`00bafed4`](#insn-00bafed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafecc`](#insn-00bafecc) → `010a2d58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafed0`](#insn-00bafed0) → `010a2d50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bafedc`](#insn-00bafedc) → `010a2d49`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bafee4`](#insn-00bafee4) → `010a2d60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafee8`](#insn-00bafee8) → [`00baff00`](#insn-00baff00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafef8`](#insn-00bafef8) → `010a2d60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafefc`](#insn-00bafefc) → [`00baff14`](#insn-00baff14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff0c`](#insn-00baff0c) → `010a2d70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baff10`](#insn-00baff10) → `010a2d68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baff1c`](#insn-00baff1c) → `010a2d61`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00baff24`](#insn-00baff24) → `010a2d78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baff28`](#insn-00baff28) → [`00baff40`](#insn-00baff40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff38`](#insn-00baff38) → `010a2d78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baff3c`](#insn-00baff3c) → [`00baff54`](#insn-00baff54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff4c`](#insn-00baff4c) → `010a2d88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baff50`](#insn-00baff50) → `010a2d80`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baff5c`](#insn-00baff5c) → `010a2d79`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00baff64`](#insn-00baff64) → `010a2d90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baff68`](#insn-00baff68) → [`00baff80`](#insn-00baff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff78`](#insn-00baff78) → `010a2d90`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baff7c`](#insn-00baff7c) → [`00baff94`](#insn-00baff94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff8c`](#insn-00baff8c) → `010a2da0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baff90`](#insn-00baff90) → `010a2d98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baff9c`](#insn-00baff9c) → `010a2d91`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00baffa4`](#insn-00baffa4) → `010a2da8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baffa8`](#insn-00baffa8) → [`00baffc0`](#insn-00baffc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffb8`](#insn-00baffb8) → `010a2da8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baffbc`](#insn-00baffbc) → [`00baffd4`](#insn-00baffd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffcc`](#insn-00baffcc) → `010a2db8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baffd0`](#insn-00baffd0) → `010a2db0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baffdc`](#insn-00baffdc) → `010a2da9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00baffe4`](#insn-00baffe4) → `010a2dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00baffe8`](#insn-00baffe8) → [`00bb0000`](#insn-00bb0000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafff8`](#insn-00bafff8) → `010a2dc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bafffc`](#insn-00bafffc) → [`00bb0014`](#insn-00bb0014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb000c`](#insn-00bb000c) → `010a2dd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0010`](#insn-00bb0010) → `010a2dc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb001c`](#insn-00bb001c) → `010a2dc1`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bb0024`](#insn-00bb0024) → `010a2dd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0028`](#insn-00bb0028) → [`00bb0040`](#insn-00bb0040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0038`](#insn-00bb0038) → `010a2dd8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb003c`](#insn-00bb003c) → [`00bb0054`](#insn-00bb0054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb004c`](#insn-00bb004c) → `010a2de8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb0050`](#insn-00bb0050) → `010a2de0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb005c`](#insn-00bb005c) → `010a2dd9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bb0060`](#insn-00bb0060) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0070`](#insn-00bb0070) → `010a2df0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb0074`](#insn-00bb0074) → [`00bdb000`](../00bdb/00bdb000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb000` · 推定シンボル `None` · 推定型 `None`
- [`00bb0078`](#insn-00bb0078) → [`00bafc88`](#insn-00bafc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0080`](#insn-00bb0080) → [`00bb8d30`](../00bb8/00bb8d30.md) · `PARAM` · `ANALYSIS` · 関数 `00bb8d30` · 推定シンボル `None` · 推定型 `None`
- [`00bb0088`](#insn-00bb0088) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb0090`](#insn-00bb0090) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00bb0098`](#insn-00bb0098) → `010a2df0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb009c`](#insn-00bb009c) → [`00bdb020`](../00bdb/00bdb020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb020` · 推定シンボル `None` · 推定型 `None`
- [`00bb00a0`](#insn-00bb00a0) → [`00bafc88`](#insn-00bafc88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafc70`](#insn-00bafc70)

~~~json
{
  "source": "00bafc70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc80`](#insn-00bafc80)

~~~json
{
  "source": "00bafc80",
  "target": "010a2df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2df0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafc84`](#insn-00bafc84)

~~~json
{
  "source": "00bafc84",
  "target": "00bb006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc8c`](#insn-00bafc8c)

~~~json
{
  "source": "00bafc8c",
  "target": "010a2ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafc90`](#insn-00bafc90)

~~~json
{
  "source": "00bafc90",
  "target": "00bafca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafca0`](#insn-00bafca0)

~~~json
{
  "source": "00bafca0",
  "target": "010a2ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafca4`](#insn-00bafca4)

~~~json
{
  "source": "00bafca4",
  "target": "00bafcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcb4`](#insn-00bafcb4)

~~~json
{
  "source": "00bafcb4",
  "target": "010a2cb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafcb8`](#insn-00bafcb8)

~~~json
{
  "source": "00bafcb8",
  "target": "010a2ca8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafcc4`](#insn-00bafcc4)

~~~json
{
  "source": "00bafcc4",
  "target": "010a2ca7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca7",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafccc`](#insn-00bafccc)

~~~json
{
  "source": "00bafccc",
  "target": "010a2ca5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca5",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafcd4`](#insn-00bafcd4)

~~~json
{
  "source": "00bafcd4",
  "target": "010a2ca1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ca1",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafcd8`](#insn-00bafcd8)

~~~json
{
  "source": "00bafcd8",
  "target": "010a2cb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cb8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafcdc`](#insn-00bafcdc)

~~~json
{
  "source": "00bafcdc",
  "target": "00bafcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcec`](#insn-00bafcec)

~~~json
{
  "source": "00bafcec",
  "target": "010a2cb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cb8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafcf0`](#insn-00bafcf0)

~~~json
{
  "source": "00bafcf0",
  "target": "00bafd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd00`](#insn-00bafd00)

~~~json
{
  "source": "00bafd00",
  "target": "010a2cc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd04`](#insn-00bafd04)

~~~json
{
  "source": "00bafd04",
  "target": "010a2cc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd10`](#insn-00bafd10)

~~~json
{
  "source": "00bafd10",
  "target": "010a2cbf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cbf",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd18`](#insn-00bafd18)

~~~json
{
  "source": "00bafd18",
  "target": "010a2cbd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cbd",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd20`](#insn-00bafd20)

~~~json
{
  "source": "00bafd20",
  "target": "010a2cb9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cb9",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd24`](#insn-00bafd24)

~~~json
{
  "source": "00bafd24",
  "target": "010a2cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd28`](#insn-00bafd28)

~~~json
{
  "source": "00bafd28",
  "target": "00bafd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd38`](#insn-00bafd38)

~~~json
{
  "source": "00bafd38",
  "target": "010a2cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd3c`](#insn-00bafd3c)

~~~json
{
  "source": "00bafd3c",
  "target": "00bafd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd4c`](#insn-00bafd4c)

~~~json
{
  "source": "00bafd4c",
  "target": "010a2ce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ce0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd50`](#insn-00bafd50)

~~~json
{
  "source": "00bafd50",
  "target": "010a2cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd5c`](#insn-00bafd5c)

~~~json
{
  "source": "00bafd5c",
  "target": "010a2cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd68`](#insn-00bafd68)

~~~json
{
  "source": "00bafd68",
  "target": "010a2cd4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd1",
  "offset": 3,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd70`](#insn-00bafd70)

~~~json
{
  "source": "00bafd70",
  "target": "010a2cd1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cd1",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd74`](#insn-00bafd74)

~~~json
{
  "source": "00bafd74",
  "target": "010a2ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ce8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd78`](#insn-00bafd78)

~~~json
{
  "source": "00bafd78",
  "target": "00bafd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd88`](#insn-00bafd88)

~~~json
{
  "source": "00bafd88",
  "target": "010a2ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ce8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafd8c`](#insn-00bafd8c)

~~~json
{
  "source": "00bafd8c",
  "target": "00bafda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd9c`](#insn-00bafd9c)

~~~json
{
  "source": "00bafd9c",
  "target": "010a2cf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafda0`](#insn-00bafda0)

~~~json
{
  "source": "00bafda0",
  "target": "010a2cf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ce9",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdb0`](#insn-00bafdb0)

~~~json
{
  "source": "00bafdb0",
  "target": "002a8090",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8090",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "5765646e657364617900",
  "capture_start": "002a8090",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bafdb4`](#insn-00bafdb4)

~~~json
{
  "source": "00bafdb4",
  "target": "010a2cf1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2cf1",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdb8`](#insn-00bafdb8)

~~~json
{
  "source": "00bafdb8",
  "target": "010a2ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ce9",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdc0`](#insn-00bafdc0)

~~~json
{
  "source": "00bafdc0",
  "target": "010a2d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdc4`](#insn-00bafdc4)

~~~json
{
  "source": "00bafdc4",
  "target": "00bafddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdd4`](#insn-00bafdd4)

~~~json
{
  "source": "00bafdd4",
  "target": "010a2d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdd8`](#insn-00bafdd8)

~~~json
{
  "source": "00bafdd8",
  "target": "00bafdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafde8`](#insn-00bafde8)

~~~json
{
  "source": "00bafde8",
  "target": "010a2d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdec`](#insn-00bafdec)

~~~json
{
  "source": "00bafdec",
  "target": "010a2d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d01",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafdf4`](#insn-00bafdf4)

~~~json
{
  "source": "00bafdf4",
  "target": "010a2d09",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d09",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe04`](#insn-00bafe04)

~~~json
{
  "source": "00bafe04",
  "target": "010a2d01",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d01",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe0c`](#insn-00bafe0c)

~~~json
{
  "source": "00bafe0c",
  "target": "010a2d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d18",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe10`](#insn-00bafe10)

~~~json
{
  "source": "00bafe10",
  "target": "00bafe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe20`](#insn-00bafe20)

~~~json
{
  "source": "00bafe20",
  "target": "010a2d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d18",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe24`](#insn-00bafe24)

~~~json
{
  "source": "00bafe24",
  "target": "00bafe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe34`](#insn-00bafe34)

~~~json
{
  "source": "00bafe34",
  "target": "010a2d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe38`](#insn-00bafe38)

~~~json
{
  "source": "00bafe38",
  "target": "010a2d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe44`](#insn-00bafe44)

~~~json
{
  "source": "00bafe44",
  "target": "010a2d1f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d1f",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe4c`](#insn-00bafe4c)

~~~json
{
  "source": "00bafe4c",
  "target": "010a2d1d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d1d",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe54`](#insn-00bafe54)

~~~json
{
  "source": "00bafe54",
  "target": "010a2d19",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d19",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe58`](#insn-00bafe58)

~~~json
{
  "source": "00bafe58",
  "target": "010a2d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe5c`](#insn-00bafe5c)

~~~json
{
  "source": "00bafe5c",
  "target": "00bafe74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe6c`](#insn-00bafe6c)

~~~json
{
  "source": "00bafe6c",
  "target": "010a2d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe70`](#insn-00bafe70)

~~~json
{
  "source": "00bafe70",
  "target": "00bafe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe80`](#insn-00bafe80)

~~~json
{
  "source": "00bafe80",
  "target": "010a2d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe84`](#insn-00bafe84)

~~~json
{
  "source": "00bafe84",
  "target": "010a2d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d31",
  "offset": 7,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe8c`](#insn-00bafe8c)

~~~json
{
  "source": "00bafe8c",
  "target": "010a2d39",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d39",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafe9c`](#insn-00bafe9c)

~~~json
{
  "source": "00bafe9c",
  "target": "010a2d31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d31",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafea4`](#insn-00bafea4)

~~~json
{
  "source": "00bafea4",
  "target": "010a2d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d48",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafea8`](#insn-00bafea8)

~~~json
{
  "source": "00bafea8",
  "target": "00bafec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafeb8`](#insn-00bafeb8)

~~~json
{
  "source": "00bafeb8",
  "target": "010a2d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d48",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafebc`](#insn-00bafebc)

~~~json
{
  "source": "00bafebc",
  "target": "00bafed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafecc`](#insn-00bafecc)

~~~json
{
  "source": "00bafecc",
  "target": "010a2d58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafed0`](#insn-00bafed0)

~~~json
{
  "source": "00bafed0",
  "target": "010a2d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafedc`](#insn-00bafedc)

~~~json
{
  "source": "00bafedc",
  "target": "010a2d49",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d49",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafee4`](#insn-00bafee4)

~~~json
{
  "source": "00bafee4",
  "target": "010a2d60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafee8`](#insn-00bafee8)

~~~json
{
  "source": "00bafee8",
  "target": "00baff00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafef8`](#insn-00bafef8)

~~~json
{
  "source": "00bafef8",
  "target": "010a2d60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d60",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafefc`](#insn-00bafefc)

~~~json
{
  "source": "00bafefc",
  "target": "00baff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff0c`](#insn-00baff0c)

~~~json
{
  "source": "00baff0c",
  "target": "010a2d70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff10`](#insn-00baff10)

~~~json
{
  "source": "00baff10",
  "target": "010a2d68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff1c`](#insn-00baff1c)

~~~json
{
  "source": "00baff1c",
  "target": "010a2d61",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d61",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff24`](#insn-00baff24)

~~~json
{
  "source": "00baff24",
  "target": "010a2d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff28`](#insn-00baff28)

~~~json
{
  "source": "00baff28",
  "target": "00baff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff38`](#insn-00baff38)

~~~json
{
  "source": "00baff38",
  "target": "010a2d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff3c`](#insn-00baff3c)

~~~json
{
  "source": "00baff3c",
  "target": "00baff54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff4c`](#insn-00baff4c)

~~~json
{
  "source": "00baff4c",
  "target": "010a2d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff50`](#insn-00baff50)

~~~json
{
  "source": "00baff50",
  "target": "010a2d80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d80",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff5c`](#insn-00baff5c)

~~~json
{
  "source": "00baff5c",
  "target": "010a2d79",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d79",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff64`](#insn-00baff64)

~~~json
{
  "source": "00baff64",
  "target": "010a2d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff68`](#insn-00baff68)

~~~json
{
  "source": "00baff68",
  "target": "00baff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff78`](#insn-00baff78)

~~~json
{
  "source": "00baff78",
  "target": "010a2d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff7c`](#insn-00baff7c)

~~~json
{
  "source": "00baff7c",
  "target": "00baff94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff8c`](#insn-00baff8c)

~~~json
{
  "source": "00baff8c",
  "target": "010a2da0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2da0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff90`](#insn-00baff90)

~~~json
{
  "source": "00baff90",
  "target": "010a2d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baff9c`](#insn-00baff9c)

~~~json
{
  "source": "00baff9c",
  "target": "010a2d91",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2d91",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffa4`](#insn-00baffa4)

~~~json
{
  "source": "00baffa4",
  "target": "010a2da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2da8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffa8`](#insn-00baffa8)

~~~json
{
  "source": "00baffa8",
  "target": "00baffc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffb8`](#insn-00baffb8)

~~~json
{
  "source": "00baffb8",
  "target": "010a2da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2da8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffbc`](#insn-00baffbc)

~~~json
{
  "source": "00baffbc",
  "target": "00baffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffcc`](#insn-00baffcc)

~~~json
{
  "source": "00baffcc",
  "target": "010a2db8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2db8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffd0`](#insn-00baffd0)

~~~json
{
  "source": "00baffd0",
  "target": "010a2db0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2db0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffdc`](#insn-00baffdc)

~~~json
{
  "source": "00baffdc",
  "target": "010a2da9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2da9",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffe4`](#insn-00baffe4)

~~~json
{
  "source": "00baffe4",
  "target": "010a2dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baffe8`](#insn-00baffe8)

~~~json
{
  "source": "00baffe8",
  "target": "00bb0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafff8`](#insn-00bafff8)

~~~json
{
  "source": "00bafff8",
  "target": "010a2dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bafffc`](#insn-00bafffc)

~~~json
{
  "source": "00bafffc",
  "target": "00bb0014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb000c`](#insn-00bb000c)

~~~json
{
  "source": "00bb000c",
  "target": "010a2dd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0010`](#insn-00bb0010)

~~~json
{
  "source": "00bb0010",
  "target": "010a2dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb001c`](#insn-00bb001c)

~~~json
{
  "source": "00bb001c",
  "target": "010a2dc1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dc1",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0024`](#insn-00bb0024)

~~~json
{
  "source": "00bb0024",
  "target": "010a2dd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0028`](#insn-00bb0028)

~~~json
{
  "source": "00bb0028",
  "target": "00bb0040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0038`](#insn-00bb0038)

~~~json
{
  "source": "00bb0038",
  "target": "010a2dd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb003c`](#insn-00bb003c)

~~~json
{
  "source": "00bb003c",
  "target": "00bb0054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb004c`](#insn-00bb004c)

~~~json
{
  "source": "00bb004c",
  "target": "010a2de8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2de8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0050`](#insn-00bb0050)

~~~json
{
  "source": "00bb0050",
  "target": "010a2de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb005c`](#insn-00bb005c)

~~~json
{
  "source": "00bb005c",
  "target": "010a2dd9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2dd9",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0060`](#insn-00bb0060)

~~~json
{
  "source": "00bb0060",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0070`](#insn-00bb0070)

~~~json
{
  "source": "00bb0070",
  "target": "010a2df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2df0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb0074`](#insn-00bb0074)

~~~json
{
  "source": "00bb0074",
  "target": "00bdb000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0078`](#insn-00bb0078)

~~~json
{
  "source": "00bb0078",
  "target": "00bafc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0080`](#insn-00bb0080)

~~~json
{
  "source": "00bb0080",
  "target": "00bb8d30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0088`](#insn-00bb0088)

~~~json
{
  "source": "00bb0088",
  "target": "00be5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb0090`](#insn-00bb0090)

~~~json
{
  "source": "00bb0090",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0098`](#insn-00bb0098)

~~~json
{
  "source": "00bb0098",
  "target": "010a2df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2df0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb009c`](#insn-00bb009c)

~~~json
{
  "source": "00bb009c",
  "target": "00bdb020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb00a0`](#insn-00bb00a0)

~~~json
{
  "source": "00bb00a0",
  "target": "00bafc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
