# 00bbc4bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbc478`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc478.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-f1068db90c6d62fa38338e4934b87736)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c38f04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38f04.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-28a01c41d19ccc83aa175d41f22c4534)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbc4bc",
  "name": "FUN_00bbc4bc",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32fa779c2f54bd1397fca2c97ffabe5012b2d02a149589f0e3ebeaa1ac5a1dd3",
  "source_text_sha256": "32fa779c2f54bd1397fca2c97ffabe5012b2d02a149589f0e3ebeaa1ac5a1dd3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbc4bc",
        "00bbc66b"
      ]
    ],
    "bytes_sha256": "f37fe67ad1760f63e1ff08c802fbb1d269749b0ef2ec075101de10849ddc77d6",
    "instruction_count": 108,
    "instruction_bytes": 432,
    "body_bytes": 432,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde9d0](../00bde/00bde9d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2866 bytes

~~~c

void FUN_00bbc4bc(long param_1,long *param_2,long param_3,ulong param_4,uint param_5)

{
  int iVar1;
  long lVar2;
  char *__s1;
  
                    /* try { // try from 00bbc4c8 to 00cbc4d3 has its CatchHandler @ 00bbd318 */
  lVar2 = param_2[2];
  if ((param_5 & 1) == 0) {
                    /* try { // try from 00bbc59c to 00cbc5a3 has its CatchHandler @ 00bbd150 */
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) {
      if (*(long *)(param_1 + 8) != *(long *)(*param_2 + 8)) {
LAB_00bbc5bc:
                    /* try { // try from 00bbc5c4 to 00cbc5d3 has its CatchHandler @ 00bbd140 */
                    /* try { // try from 00bbc5d4 to 00cbc5e7 has its CatchHandler @ 00bbd128 */
                    /* WARNING: Could not recover jumptable at 0x00bbc5e8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (**(code **)(**(long **)(param_1 + 0x10) + 0x30))
                  (*(long **)(param_1 + 0x10),param_2,param_3,param_4,param_5 & 1);
        return;
      }
LAB_00bbc530:
      if ((param_2[4] == param_3) || (param_2[5] == param_3)) {
                    /* try { // try from 00bbc610 to 00cbc617 has its CatchHandler @ 00bbd3c4 */
        if ((int)param_4 != 1) {
          return;
        }
                    /* try { // try from 00bbc618 to 00cbc693 has its CatchHandler @ 00bbd424 */
        *(undefined4 *)(param_2 + 7) = 1;
        return;
      }
      *(int *)(param_2 + 7) = (int)param_4;
      if (*(int *)((long)param_2 + 0x44) != 4) {
        *(undefined2 *)((long)param_2 + 0x4c) = 0;
        (**(code **)(**(long **)(param_1 + 0x10) + 0x28))
                  (*(long **)(param_1 + 0x10),param_2,param_3,param_3,1,param_5 & 1);
        if (*(char *)((long)param_2 + 0x4d) == '\0') {
          *(undefined4 *)((long)param_2 + 0x44) = 4;
        }
        else {
          *(undefined4 *)((long)param_2 + 0x44) = 3;
                    /* try { // try from 00bbc594 to 00cbc59b has its CatchHandler @ 00bbd32c */
          if (*(char *)((long)param_2 + 0x4c) != '\0') {
            return;
          }
        }
      }
      param_2[5] = param_3;
      *(int *)(param_2 + 8) = (int)param_2[8] + 1;
      if (*(int *)((long)param_2 + 0x3c) != 1) {
        return;
      }
      if ((int)param_2[6] != 2) {
        return;
      }
      *(undefined1 *)((long)param_2 + 0x4e) = 1;
      return;
    }
  }
  else if (lVar2 != param_1) {
    __s1 = *(char **)(param_1 + 8);
    param_4 = param_4 & 0xffffffff;
    iVar1 = strcmp(__s1,*(char **)(lVar2 + 8));
    if (iVar1 != 0) {
      if ((*param_2 != param_1) && (iVar1 = strcmp(__s1,*(char **)(*param_2 + 8)), iVar1 != 0))
      goto LAB_00bbc5bc;
      goto LAB_00bbc530;
    }
  }
  if ((param_2[1] == param_3) && (*(int *)((long)param_2 + 0x34) != 1)) {
    *(int *)((long)param_2 + 0x34) = (int)param_4;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbc4bc"></a> `00bbc4bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbc4c0"></a> `00bbc4c0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbc4c4"></a> `00bbc4c4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc4c8"></a> `00bbc4c8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc4cc"></a> `00bbc4cc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc4d0"></a> `00bbc4d0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbc4d4"></a> `00bbc4d4` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc4d8"></a> `00bbc4d8` | `f5 03 04 2a` | mov w21,w4 | `FALL_THROUGH`
<a id="insn-00bbc4dc"></a> `00bbc4dc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bbc4e0"></a> `00bbc4e0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbc4e4"></a> `00bbc4e4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbc4e8"></a> `00bbc4e8` | `a4 05 00 36` | tbz w4,#0x0,0x00bbc59c | `CONDITIONAL_JUMP`
<a id="insn-00bbc4ec"></a> `00bbc4ec` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bbc4f0"></a> `00bbc4f0` | `e0 07 00 54` | b.eq 0x00bbc5ec | `CONDITIONAL_JUMP`
<a id="insn-00bbc4f4"></a> `00bbc4f4` | `d7 06 40 f9` | ldr x23,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc4f8"></a> `00bbc4f8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc4fc"></a> `00bbc4fc` | `f8 03 03 2a` | mov w24,w3 | `FALL_THROUGH`
<a id="insn-00bbc500"></a> `00bbc500` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbc504"></a> `00bbc504` | `33 89 00 94` | bl 0x00bde9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc508"></a> `00bbc508` | `e3 03 18 2a` | mov w3,w24 | `FALL_THROUGH`
<a id="insn-00bbc50c"></a> `00bbc50c` | `00 07 00 34` | cbz w0,0x00bbc5ec | `CONDITIONAL_JUMP`
<a id="insn-00bbc510"></a> `00bbc510` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbc514"></a> `00bbc514` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bbc518"></a> `00bbc518` | `c0 00 00 54` | b.eq 0x00bbc530 | `CONDITIONAL_JUMP`
<a id="insn-00bbc51c"></a> `00bbc51c` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc520"></a> `00bbc520` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbc524"></a> `00bbc524` | `2b 89 00 94` | bl 0x00bde9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc528"></a> `00bbc528` | `e3 03 18 2a` | mov w3,w24 | `FALL_THROUGH`
<a id="insn-00bbc52c"></a> `00bbc52c` | `80 04 00 35` | cbnz w0,0x00bbc5bc | `CONDITIONAL_JUMP`
<a id="insn-00bbc530"></a> `00bbc530` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc534"></a> `00bbc534` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bbc538"></a> `00bbc538` | `a0 06 00 54` | b.eq 0x00bbc60c | `CONDITIONAL_JUMP`
<a id="insn-00bbc53c"></a> `00bbc53c` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc540"></a> `00bbc540` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bbc544"></a> `00bbc544` | `40 06 00 54` | b.eq 0x00bbc60c | `CONDITIONAL_JUMP`
<a id="insn-00bbc548"></a> `00bbc548` | `68 46 40 b9` | ldr w8,[x19, #0x44] | `FALL_THROUGH`
<a id="insn-00bbc54c"></a> `00bbc54c` | `63 3a 00 b9` | str w3,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbc550"></a> `00bbc550` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbc554"></a> `00bbc554` | `a0 06 00 54` | b.eq 0x00bbc628 | `CONDITIONAL_JUMP`
<a id="insn-00bbc558"></a> `00bbc558` | `7f 9a 00 79` | strh wzr,[x19, #0x4c] | `FALL_THROUGH`
<a id="insn-00bbc55c"></a> `00bbc55c` | `a5 02 00 12` | and w5,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc560"></a> `00bbc560` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbc564"></a> `00bbc564` | `c0 0a 40 f9` | ldr x0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc568"></a> `00bbc568` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bbc56c"></a> `00bbc56c` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbc570"></a> `00bbc570` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc574"></a> `00bbc574` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbc578"></a> `00bbc578` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc57c"></a> `00bbc57c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbc580"></a> `00bbc580` | `68 36 41 39` | ldrb w8,[x19, #0x4d] | `FALL_THROUGH`
<a id="insn-00bbc584"></a> `00bbc584` | `e8 04 00 34` | cbz w8,0x00bbc620 | `CONDITIONAL_JUMP`
<a id="insn-00bbc588"></a> `00bbc588` | `68 32 41 39` | ldrb w8,[x19, #0x4c] | `FALL_THROUGH`
<a id="insn-00bbc58c"></a> `00bbc58c` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbc590"></a> `00bbc590` | `69 46 00 b9` | str w9,[x19, #0x44] | `FALL_THROUGH`
<a id="insn-00bbc594"></a> `00bbc594` | `08 06 00 35` | cbnz w8,0x00bbc654 | `CONDITIONAL_JUMP`
<a id="insn-00bbc598"></a> `00bbc598` | `24 00 00 14` | b 0x00bbc628 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc59c"></a> `00bbc59c` | `c9 06 40 f9` | ldr x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc5a0"></a> `00bbc5a0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc5a4"></a> `00bbc5a4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbc5a8"></a> `00bbc5a8` | `20 02 00 54` | b.eq 0x00bbc5ec | `CONDITIONAL_JUMP`
<a id="insn-00bbc5ac"></a> `00bbc5ac` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbc5b0"></a> `00bbc5b0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc5b4"></a> `00bbc5b4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbc5b8"></a> `00bbc5b8` | `c0 fb ff 54` | b.eq 0x00bbc530 | `CONDITIONAL_JUMP`
<a id="insn-00bbc5bc"></a> `00bbc5bc` | `c0 0a 40 f9` | ldr x0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc5c0"></a> `00bbc5c0` | `a4 02 00 12` | and w4,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc5c4"></a> `00bbc5c4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbc5c8"></a> `00bbc5c8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbc5cc"></a> `00bbc5cc` | `10 19 40 f9` | ldr x16,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc5d0"></a> `00bbc5d0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bbc5d4"></a> `00bbc5d4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc5d8"></a> `00bbc5d8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc5dc"></a> `00bbc5dc` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc5e0"></a> `00bbc5e0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbc5e4"></a> `00bbc5e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbc5e8"></a> `00bbc5e8` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bbc5ec"></a> `00bbc5ec` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc5f0"></a> `00bbc5f0` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bbc5f4"></a> `00bbc5f4` | `01 03 00 54` | b.ne 0x00bbc654 | `CONDITIONAL_JUMP`
<a id="insn-00bbc5f8"></a> `00bbc5f8` | `68 36 40 b9` | ldr w8,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00bbc5fc"></a> `00bbc5fc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc600"></a> `00bbc600` | `a0 02 00 54` | b.eq 0x00bbc654 | `CONDITIONAL_JUMP`
<a id="insn-00bbc604"></a> `00bbc604` | `63 36 00 b9` | str w3,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00bbc608"></a> `00bbc608` | `13 00 00 14` | b 0x00bbc654 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc60c"></a> `00bbc60c` | `7f 04 00 71` | cmp w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc610"></a> `00bbc610` | `21 02 00 54` | b.ne 0x00bbc654 | `CONDITIONAL_JUMP`
<a id="insn-00bbc614"></a> `00bbc614` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc618"></a> `00bbc618` | `68 3a 00 b9` | str w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbc61c"></a> `00bbc61c` | `0e 00 00 14` | b 0x00bbc654 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc620"></a> `00bbc620` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbc624"></a> `00bbc624` | `68 46 00 b9` | str w8,[x19, #0x44] | `FALL_THROUGH`
<a id="insn-00bbc628"></a> `00bbc628` | `69 a2 47 29` | ldp w9,w8,[x19, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbc62c"></a> `00bbc62c` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc630"></a> `00bbc630` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc634"></a> `00bbc634` | `3f 05 00 71` | cmp w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc638"></a> `00bbc638` | `68 42 00 b9` | str w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bbc63c"></a> `00bbc63c` | `c1 00 00 54` | b.ne 0x00bbc654 | `CONDITIONAL_JUMP`
<a id="insn-00bbc640"></a> `00bbc640` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc644"></a> `00bbc644` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbc648"></a> `00bbc648` | `61 00 00 54` | b.ne 0x00bbc654 | `CONDITIONAL_JUMP`
<a id="insn-00bbc64c"></a> `00bbc64c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc650"></a> `00bbc650` | `68 3a 01 39` | strb w8,[x19, #0x4e] | `FALL_THROUGH`
<a id="insn-00bbc654"></a> `00bbc654` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc658"></a> `00bbc658` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc65c"></a> `00bbc65c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc660"></a> `00bbc660` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbc664"></a> `00bbc664` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbc668"></a> `00bbc668` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbc4bc`](#insn-00bbc4bc) 範囲 `[['00bbc4bc', '00bbc4c7']]`
  - `FALL_THROUGH` [`00bbc4c4`](#insn-00bbc4c4) → [`00bbc4c8`](#insn-00bbc4c8)
- ブロック [`00bbc4c8`](#insn-00bbc4c8) 範囲 `[['00bbc4c8', '00bbc4eb']]`
  - `CONDITIONAL_JUMP` [`00bbc4e8`](#insn-00bbc4e8) → [`00bbc59c`](#insn-00bbc59c)
  - `FALL_THROUGH` [`00bbc4e8`](#insn-00bbc4e8) → [`00bbc4ec`](#insn-00bbc4ec)
- ブロック [`00bbc4ec`](#insn-00bbc4ec) 範囲 `[['00bbc4ec', '00bbc4f3']]`
  - `CONDITIONAL_JUMP` [`00bbc4f0`](#insn-00bbc4f0) → [`00bbc5ec`](#insn-00bbc5ec)
  - `FALL_THROUGH` [`00bbc4f0`](#insn-00bbc4f0) → [`00bbc4f4`](#insn-00bbc4f4)
- ブロック [`00bbc4f4`](#insn-00bbc4f4) 範囲 `[['00bbc4f4', '00bbc50f']]`
  - `CONDITIONAL_JUMP` [`00bbc50c`](#insn-00bbc50c) → [`00bbc5ec`](#insn-00bbc5ec)
  - `FALL_THROUGH` [`00bbc50c`](#insn-00bbc50c) → [`00bbc510`](#insn-00bbc510)
- ブロック [`00bbc510`](#insn-00bbc510) 範囲 `[['00bbc510', '00bbc51b']]`
  - `CONDITIONAL_JUMP` [`00bbc518`](#insn-00bbc518) → [`00bbc530`](#insn-00bbc530)
  - `FALL_THROUGH` [`00bbc518`](#insn-00bbc518) → [`00bbc51c`](#insn-00bbc51c)
- ブロック [`00bbc51c`](#insn-00bbc51c) 範囲 `[['00bbc51c', '00bbc52f']]`
  - `CONDITIONAL_JUMP` [`00bbc52c`](#insn-00bbc52c) → [`00bbc5bc`](#insn-00bbc5bc)
  - `FALL_THROUGH` [`00bbc52c`](#insn-00bbc52c) → [`00bbc530`](#insn-00bbc530)
- ブロック [`00bbc530`](#insn-00bbc530) 範囲 `[['00bbc530', '00bbc53b']]`
  - `CONDITIONAL_JUMP` [`00bbc538`](#insn-00bbc538) → [`00bbc60c`](#insn-00bbc60c)
  - `FALL_THROUGH` [`00bbc538`](#insn-00bbc538) → [`00bbc53c`](#insn-00bbc53c)
- ブロック [`00bbc53c`](#insn-00bbc53c) 範囲 `[['00bbc53c', '00bbc547']]`
  - `CONDITIONAL_JUMP` [`00bbc544`](#insn-00bbc544) → [`00bbc60c`](#insn-00bbc60c)
  - `FALL_THROUGH` [`00bbc544`](#insn-00bbc544) → [`00bbc548`](#insn-00bbc548)
- ブロック [`00bbc548`](#insn-00bbc548) 範囲 `[['00bbc548', '00bbc557']]`
  - `CONDITIONAL_JUMP` [`00bbc554`](#insn-00bbc554) → [`00bbc628`](#insn-00bbc628)
  - `FALL_THROUGH` [`00bbc554`](#insn-00bbc554) → [`00bbc558`](#insn-00bbc558)
- ブロック [`00bbc558`](#insn-00bbc558) 範囲 `[['00bbc558', '00bbc587']]`
  - `CONDITIONAL_JUMP` [`00bbc584`](#insn-00bbc584) → [`00bbc620`](#insn-00bbc620)
  - `FALL_THROUGH` [`00bbc584`](#insn-00bbc584) → [`00bbc588`](#insn-00bbc588)
- ブロック [`00bbc588`](#insn-00bbc588) 範囲 `[['00bbc588', '00bbc593']]`
  - `FALL_THROUGH` [`00bbc590`](#insn-00bbc590) → [`00bbc594`](#insn-00bbc594)
- ブロック [`00bbc594`](#insn-00bbc594) 範囲 `[['00bbc594', '00bbc597']]`
  - `CONDITIONAL_JUMP` [`00bbc594`](#insn-00bbc594) → [`00bbc654`](#insn-00bbc654)
  - `FALL_THROUGH` [`00bbc594`](#insn-00bbc594) → [`00bbc598`](#insn-00bbc598)
- ブロック [`00bbc598`](#insn-00bbc598) 範囲 `[['00bbc598', '00bbc59b']]`
  - `UNCONDITIONAL_JUMP` [`00bbc598`](#insn-00bbc598) → [`00bbc628`](#insn-00bbc628)
- ブロック [`00bbc59c`](#insn-00bbc59c) 範囲 `[['00bbc59c', '00bbc5ab']]`
  - `CONDITIONAL_JUMP` [`00bbc5a8`](#insn-00bbc5a8) → [`00bbc5ec`](#insn-00bbc5ec)
  - `FALL_THROUGH` [`00bbc5a8`](#insn-00bbc5a8) → [`00bbc5ac`](#insn-00bbc5ac)
- ブロック [`00bbc5ac`](#insn-00bbc5ac) 範囲 `[['00bbc5ac', '00bbc5bb']]`
  - `CONDITIONAL_JUMP` [`00bbc5b8`](#insn-00bbc5b8) → [`00bbc530`](#insn-00bbc530)
  - `FALL_THROUGH` [`00bbc5b8`](#insn-00bbc5b8) → [`00bbc5bc`](#insn-00bbc5bc)
- ブロック [`00bbc5bc`](#insn-00bbc5bc) 範囲 `[['00bbc5bc', '00bbc5c3']]`
  - `FALL_THROUGH` [`00bbc5c0`](#insn-00bbc5c0) → [`00bbc5c4`](#insn-00bbc5c4)
- ブロック [`00bbc5c4`](#insn-00bbc5c4) 範囲 `[['00bbc5c4', '00bbc5d3']]`
  - `FALL_THROUGH` [`00bbc5d0`](#insn-00bbc5d0) → [`00bbc5d4`](#insn-00bbc5d4)
- ブロック [`00bbc5d4`](#insn-00bbc5d4) 範囲 `[['00bbc5d4', '00bbc5eb']]`
- ブロック [`00bbc5ec`](#insn-00bbc5ec) 範囲 `[['00bbc5ec', '00bbc5f7']]`
  - `CONDITIONAL_JUMP` [`00bbc5f4`](#insn-00bbc5f4) → [`00bbc654`](#insn-00bbc654)
  - `FALL_THROUGH` [`00bbc5f4`](#insn-00bbc5f4) → [`00bbc5f8`](#insn-00bbc5f8)
- ブロック [`00bbc5f8`](#insn-00bbc5f8) 範囲 `[['00bbc5f8', '00bbc603']]`
  - `CONDITIONAL_JUMP` [`00bbc600`](#insn-00bbc600) → [`00bbc654`](#insn-00bbc654)
  - `FALL_THROUGH` [`00bbc600`](#insn-00bbc600) → [`00bbc604`](#insn-00bbc604)
- ブロック [`00bbc604`](#insn-00bbc604) 範囲 `[['00bbc604', '00bbc60b']]`
  - `UNCONDITIONAL_JUMP` [`00bbc608`](#insn-00bbc608) → [`00bbc654`](#insn-00bbc654)
- ブロック [`00bbc60c`](#insn-00bbc60c) 範囲 `[['00bbc60c', '00bbc60f']]`
  - `FALL_THROUGH` [`00bbc60c`](#insn-00bbc60c) → [`00bbc610`](#insn-00bbc610)
- ブロック [`00bbc610`](#insn-00bbc610) 範囲 `[['00bbc610', '00bbc613']]`
  - `CONDITIONAL_JUMP` [`00bbc610`](#insn-00bbc610) → [`00bbc654`](#insn-00bbc654)
  - `FALL_THROUGH` [`00bbc610`](#insn-00bbc610) → [`00bbc614`](#insn-00bbc614)
- ブロック [`00bbc614`](#insn-00bbc614) 範囲 `[['00bbc614', '00bbc617']]`
  - `FALL_THROUGH` [`00bbc614`](#insn-00bbc614) → [`00bbc618`](#insn-00bbc618)
- ブロック [`00bbc618`](#insn-00bbc618) 範囲 `[['00bbc618', '00bbc61f']]`
  - `UNCONDITIONAL_JUMP` [`00bbc61c`](#insn-00bbc61c) → [`00bbc654`](#insn-00bbc654)
- ブロック [`00bbc620`](#insn-00bbc620) 範囲 `[['00bbc620', '00bbc627']]`
  - `FALL_THROUGH` [`00bbc624`](#insn-00bbc624) → [`00bbc628`](#insn-00bbc628)
- ブロック [`00bbc628`](#insn-00bbc628) 範囲 `[['00bbc628', '00bbc63f']]`
  - `CONDITIONAL_JUMP` [`00bbc63c`](#insn-00bbc63c) → [`00bbc654`](#insn-00bbc654)
  - `FALL_THROUGH` [`00bbc63c`](#insn-00bbc63c) → [`00bbc640`](#insn-00bbc640)
- ブロック [`00bbc640`](#insn-00bbc640) 範囲 `[['00bbc640', '00bbc64b']]`
  - `CONDITIONAL_JUMP` [`00bbc648`](#insn-00bbc648) → [`00bbc654`](#insn-00bbc654)
  - `FALL_THROUGH` [`00bbc648`](#insn-00bbc648) → [`00bbc64c`](#insn-00bbc64c)
- ブロック [`00bbc64c`](#insn-00bbc64c) 範囲 `[['00bbc64c', '00bbc653']]`
  - `FALL_THROUGH` [`00bbc650`](#insn-00bbc650) → [`00bbc654`](#insn-00bbc654)
- ブロック [`00bbc654`](#insn-00bbc654) 範囲 `[['00bbc654', '00bbc66b']]`

## 命令位置別の参照

- [`00bbc4c0`](#insn-00bbc4c0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc4c4`](#insn-00bbc4c4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc4c8`](#insn-00bbc4c8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc4cc`](#insn-00bbc4cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc4e8`](#insn-00bbc4e8) → [`00bbc59c`](#insn-00bbc59c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc4f0`](#insn-00bbc4f0) → [`00bbc5ec`](#insn-00bbc5ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc504`](#insn-00bbc504) → [`00bde9d0`](../00bde/00bde9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc50c`](#insn-00bbc50c) → [`00bbc5ec`](#insn-00bbc5ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc518`](#insn-00bbc518) → [`00bbc530`](#insn-00bbc530) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc524`](#insn-00bbc524) → [`00bde9d0`](../00bde/00bde9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc52c`](#insn-00bbc52c) → [`00bbc5bc`](#insn-00bbc5bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc538`](#insn-00bbc538) → [`00bbc60c`](#insn-00bbc60c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc544`](#insn-00bbc544) → [`00bbc60c`](#insn-00bbc60c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc554`](#insn-00bbc554) → [`00bbc628`](#insn-00bbc628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc584`](#insn-00bbc584) → [`00bbc620`](#insn-00bbc620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc594`](#insn-00bbc594) → [`00bbc654`](#insn-00bbc654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc598`](#insn-00bbc598) → [`00bbc628`](#insn-00bbc628) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5a8`](#insn-00bbc5a8) → [`00bbc5ec`](#insn-00bbc5ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5b8`](#insn-00bbc5b8) → [`00bbc530`](#insn-00bbc530) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5d4`](#insn-00bbc5d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5d8`](#insn-00bbc5d8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5dc`](#insn-00bbc5dc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5e0`](#insn-00bbc5e0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc5f4`](#insn-00bbc5f4) → [`00bbc654`](#insn-00bbc654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc600`](#insn-00bbc600) → [`00bbc654`](#insn-00bbc654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc608`](#insn-00bbc608) → [`00bbc654`](#insn-00bbc654) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc610`](#insn-00bbc610) → [`00bbc654`](#insn-00bbc654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc61c`](#insn-00bbc61c) → [`00bbc654`](#insn-00bbc654) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc63c`](#insn-00bbc63c) → [`00bbc654`](#insn-00bbc654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc648`](#insn-00bbc648) → [`00bbc654`](#insn-00bbc654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc654`](#insn-00bbc654) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc658`](#insn-00bbc658) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc65c`](#insn-00bbc65c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc660`](#insn-00bbc660) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbc4c0`](#insn-00bbc4c0)

~~~json
{
  "source": "00bbc4c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc4c4`](#insn-00bbc4c4)

~~~json
{
  "source": "00bbc4c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc4c8`](#insn-00bbc4c8)

~~~json
{
  "source": "00bbc4c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc4cc`](#insn-00bbc4cc)

~~~json
{
  "source": "00bbc4cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc4e8`](#insn-00bbc4e8)

~~~json
{
  "source": "00bbc4e8",
  "target": "00bbc59c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc4f0`](#insn-00bbc4f0)

~~~json
{
  "source": "00bbc4f0",
  "target": "00bbc5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc504`](#insn-00bbc504)

~~~json
{
  "source": "00bbc504",
  "target": "00bde9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc50c`](#insn-00bbc50c)

~~~json
{
  "source": "00bbc50c",
  "target": "00bbc5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc518`](#insn-00bbc518)

~~~json
{
  "source": "00bbc518",
  "target": "00bbc530",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc524`](#insn-00bbc524)

~~~json
{
  "source": "00bbc524",
  "target": "00bde9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc52c`](#insn-00bbc52c)

~~~json
{
  "source": "00bbc52c",
  "target": "00bbc5bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc538`](#insn-00bbc538)

~~~json
{
  "source": "00bbc538",
  "target": "00bbc60c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc544`](#insn-00bbc544)

~~~json
{
  "source": "00bbc544",
  "target": "00bbc60c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc554`](#insn-00bbc554)

~~~json
{
  "source": "00bbc554",
  "target": "00bbc628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc584`](#insn-00bbc584)

~~~json
{
  "source": "00bbc584",
  "target": "00bbc620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc594`](#insn-00bbc594)

~~~json
{
  "source": "00bbc594",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc598`](#insn-00bbc598)

~~~json
{
  "source": "00bbc598",
  "target": "00bbc628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5a8`](#insn-00bbc5a8)

~~~json
{
  "source": "00bbc5a8",
  "target": "00bbc5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5b8`](#insn-00bbc5b8)

~~~json
{
  "source": "00bbc5b8",
  "target": "00bbc530",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5d4`](#insn-00bbc5d4)

~~~json
{
  "source": "00bbc5d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5d8`](#insn-00bbc5d8)

~~~json
{
  "source": "00bbc5d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5dc`](#insn-00bbc5dc)

~~~json
{
  "source": "00bbc5dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5e0`](#insn-00bbc5e0)

~~~json
{
  "source": "00bbc5e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc5f4`](#insn-00bbc5f4)

~~~json
{
  "source": "00bbc5f4",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc600`](#insn-00bbc600)

~~~json
{
  "source": "00bbc600",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc608`](#insn-00bbc608)

~~~json
{
  "source": "00bbc608",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc610`](#insn-00bbc610)

~~~json
{
  "source": "00bbc610",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc61c`](#insn-00bbc61c)

~~~json
{
  "source": "00bbc61c",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc63c`](#insn-00bbc63c)

~~~json
{
  "source": "00bbc63c",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc648`](#insn-00bbc648)

~~~json
{
  "source": "00bbc648",
  "target": "00bbc654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc654`](#insn-00bbc654)

~~~json
{
  "source": "00bbc654",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc658`](#insn-00bbc658)

~~~json
{
  "source": "00bbc658",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc65c`](#insn-00bbc65c)

~~~json
{
  "source": "00bbc65c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc660`](#insn-00bbc660)

~~~json
{
  "source": "00bbc660",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
