# 00aab4cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aab488`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-7329e55917a32c89bfd31438f50c6db7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0af5c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-6c077103859fef2d4ef4f27709725462)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aab4cc",
  "name": "FUN_00aab4cc",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f74a065afa1414dee1142f80120cb7d9034f1aa46d7a2af01268fe3cdc66c26",
  "source_text_sha256": "9f74a065afa1414dee1142f80120cb7d9034f1aa46d7a2af01268fe3cdc66c26",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aab4cc",
        "00aab623"
      ]
    ],
    "bytes_sha256": "e471613aa08275e3f92676ad96e3328398067a7eb2fd42df6ea43753708c278d",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005d996c](../005d9/005d996c.md)
- [0079bdf0](../0079b/0079bdf0.md)
- [007acf88](../007ac/007acf88.md)
- [00a7268c](../00a72/00a7268c.md)
- [00a788d0](../00a78/00a788d0.md)
- [00aabe48](../00aab/00aabe48.md)
- [00aad9e4](../00aad/00aad9e4.md)
- [00aadb20](../00aad/00aadb20.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1824 bytes

~~~c

int FUN_00aab4cc(long param_1,int param_2,int param_3,int param_4)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  long *plVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  if (param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_3 = FUN_007cfaa0();
    param_4 = FUN_007cfcd8();
    puVar2 = *(undefined8 **)(param_1 + 0x20);
  }
  else {
    puVar2 = *(undefined8 **)(param_1 + 0x20);
  }
  if (puVar2 != (undefined8 *)0x0) {
    param_4 = param_2 * 1000 + param_3 * 10 + param_4;
    puVar4 = puVar2;
    do {
      if (*(int *)(puVar4 + 4) <= param_4) {
        if (param_4 <= *(int *)(puVar4 + 4)) goto LAB_00aab56c;
        puVar4 = puVar4 + 1;
      }
      puVar4 = (undefined8 *)*puVar4;
    } while (puVar4 != (undefined8 *)0x0);
  }
  return 0;
LAB_00aab56c:
  puVar4 = puVar2;
  if (param_4 < *(int *)(puVar4 + 4)) {
    puVar2 = (undefined8 *)*puVar4;
    puVar5 = puVar4;
    if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00aab5a0;
    goto LAB_00aab56c;
  }
  if (param_4 <= *(int *)(puVar4 + 4)) goto LAB_00aab5f8;
  puVar2 = (undefined8 *)puVar4[1];
  if ((undefined8 *)puVar4[1] == (undefined8 *)0x0) {
    puVar5 = puVar4 + 1;
LAB_00aab5a0:
    puVar1 = (undefined8 *)_Znwm(0x40);
    puVar1[6] = 0;
    puVar1[7] = 0;
    puVar1[5] = 0;
    *puVar1 = 0;
    puVar1[1] = 0;
    puVar1[2] = puVar4;
    *puVar5 = puVar1;
    plVar3 = *(long **)(param_1 + 0x18);
    *(int *)(puVar1 + 4) = param_4;
    puVar2 = puVar1;
    if (*plVar3 != 0) {
      *(long *)(param_1 + 0x18) = *plVar3;
      puVar2 = (undefined8 *)*puVar5;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar2);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
    puVar4 = puVar1;
LAB_00aab5f8:
    return (int)((ulong)(puVar4[6] - puVar4[5]) >> 3) * -0x55555555;
  }
  goto LAB_00aab56c;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aab4cc"></a> `00aab4cc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aab4d0"></a> `00aab4d0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab4d4"></a> `00aab4d4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aab4d8"></a> `00aab4d8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aab4dc"></a> `00aab4dc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aab4e0"></a> `00aab4e0` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aab4e4"></a> `00aab4e4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aab4e8"></a> `00aab4e8` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aab4ec"></a> `00aab4ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aab4f0"></a> `00aab4f0` | `80 00 00 54` | b.eq 0x00aab500 | `CONDITIONAL_JUMP`
<a id="insn-00aab4f4"></a> `00aab4f4` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aab4f8"></a> `00aab4f8` | `68 01 00 b5` | cbnz x8,0x00aab524 | `CONDITIONAL_JUMP`
<a id="insn-00aab4fc"></a> `00aab4fc` | `26 00 00 14` | b 0x00aab594 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab500"></a> `00aab500` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aab504"></a> `00aab504` | `13 91 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aab508"></a> `00aab508` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aab50c"></a> `00aab50c` | `65 91 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab510"></a> `00aab510` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aab514"></a> `00aab514` | `f1 91 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aab518"></a> `00aab518` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aab51c"></a> `00aab51c` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aab520"></a> `00aab520` | `a8 03 00 b4` | cbz x8,0x00aab594 | `CONDITIONAL_JUMP`
<a id="insn-00aab524"></a> `00aab524` | `09 7d 80 52` | mov w9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00aab528"></a> `00aab528` | `4a 01 80 52` | mov w10,#0xa | `FALL_THROUGH`
<a id="insn-00aab52c"></a> `00aab52c` | `89 7e 09 1b` | mul w9,w20,w9 | `FALL_THROUGH`
<a id="insn-00aab530"></a> `00aab530` | `a9 26 0a 1b` | madd w9,w21,w10,w9 | `FALL_THROUGH`
<a id="insn-00aab534"></a> `00aab534` | `35 01 03 0b` | add w21,w9,w3 | `FALL_THROUGH`
<a id="insn-00aab538"></a> `00aab538` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00aab53c"></a> `00aab53c` | `03 00 00 14` | b 0x00aab548 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab540"></a> `00aab540` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aab544"></a> `00aab544` | `89 02 00 b4` | cbz x9,0x00aab594 | `CONDITIONAL_JUMP`
<a id="insn-00aab548"></a> `00aab548` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aab54c"></a> `00aab54c` | `bf 02 0a 6b` | cmp w21,w10 | `FALL_THROUGH`
<a id="insn-00aab550"></a> `00aab550` | `8b ff ff 54` | b.lt 0x00aab540 | `CONDITIONAL_JUMP`
<a id="insn-00aab554"></a> `00aab554` | `5f 01 15 6b` | cmp w10,w21 | `FALL_THROUGH`
<a id="insn-00aab558"></a> `00aab558` | `aa 00 00 54` | b.ge 0x00aab56c | `CONDITIONAL_JUMP`
<a id="insn-00aab55c"></a> `00aab55c` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00aab560"></a> `00aab560` | `f8 ff ff 17` | b 0x00aab540 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab564"></a> `00aab564` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aab568"></a> `00aab568` | `a8 01 00 b4` | cbz x8,0x00aab59c | `CONDITIONAL_JUMP`
<a id="insn-00aab56c"></a> `00aab56c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aab570"></a> `00aab570` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab574"></a> `00aab574` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00aab578"></a> `00aab578` | `6b ff ff 54` | b.lt 0x00aab564 | `CONDITIONAL_JUMP`
<a id="insn-00aab57c"></a> `00aab57c` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00aab580"></a> `00aab580` | `aa 03 00 54` | b.ge 0x00aab5f4 | `CONDITIONAL_JUMP`
<a id="insn-00aab584"></a> `00aab584` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aab588"></a> `00aab588` | `28 ff ff b5` | cbnz x8,0x00aab56c | `CONDITIONAL_JUMP`
<a id="insn-00aab58c"></a> `00aab58c` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aab590"></a> `00aab590` | `04 00 00 14` | b 0x00aab5a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab594"></a> `00aab594` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aab598"></a> `00aab598` | `1e 00 00 14` | b 0x00aab610 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab59c"></a> `00aab59c` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00aab5a0"></a> `00aab5a0` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab5a4"></a> `00aab5a4` | `a7 be 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aab5a8"></a> `00aab5a8` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab5ac"></a> `00aab5ac` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab5b0"></a> `00aab5b0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab5b4"></a> `00aab5b4` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab5b8"></a> `00aab5b8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab5bc"></a> `00aab5bc` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab5c0"></a> `00aab5c0` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00aab5c4"></a> `00aab5c4` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aab5c8"></a> `00aab5c8` | `15 20 00 b9` | str w21,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab5cc"></a> `00aab5cc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab5d0"></a> `00aab5d0` | `68 00 00 b4` | cbz x8,0x00aab5dc | `CONDITIONAL_JUMP`
<a id="insn-00aab5d4"></a> `00aab5d4` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aab5d8"></a> `00aab5d8` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00aab5dc"></a> `00aab5dc` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aab5e0"></a> `00aab5e0` | `a1 b6 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab5e4"></a> `00aab5e4` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aab5e8"></a> `00aab5e8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab5ec"></a> `00aab5ec` | `68 16 00 f9` | str x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aab5f0"></a> `00aab5f0` | `02 00 00 14` | b 0x00aab5f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab5f4"></a> `00aab5f4` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aab5f8"></a> `00aab5f8` | `89 a2 42 a9` | ldp x9,x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aab5fc"></a> `00aab5fc` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aab600"></a> `00aab600` | `69 55 95 52` | mov w9,#0xaaab | `FALL_THROUGH`
<a id="insn-00aab604"></a> `00aab604` | `08 fd 43 d3` | lsr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aab608"></a> `00aab608` | `49 55 b5 72` | movk w9,#0xaaaa, LSL #16 | `FALL_THROUGH`
<a id="insn-00aab60c"></a> `00aab60c` | `00 7d 09 1b` | mul w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00aab610"></a> `00aab610` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aab614"></a> `00aab614` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab618"></a> `00aab618` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aab61c"></a> `00aab61c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aab620"></a> `00aab620` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aab4cc`](#insn-00aab4cc) 範囲 `[['00aab4cc', '00aab4f3']]`
  - `CONDITIONAL_JUMP` [`00aab4f0`](#insn-00aab4f0) → [`00aab500`](#insn-00aab500)
  - `FALL_THROUGH` [`00aab4f0`](#insn-00aab4f0) → [`00aab4f4`](#insn-00aab4f4)
- ブロック [`00aab4f4`](#insn-00aab4f4) 範囲 `[['00aab4f4', '00aab4fb']]`
  - `CONDITIONAL_JUMP` [`00aab4f8`](#insn-00aab4f8) → [`00aab524`](#insn-00aab524)
  - `FALL_THROUGH` [`00aab4f8`](#insn-00aab4f8) → [`00aab4fc`](#insn-00aab4fc)
- ブロック [`00aab4fc`](#insn-00aab4fc) 範囲 `[['00aab4fc', '00aab4ff']]`
  - `UNCONDITIONAL_JUMP` [`00aab4fc`](#insn-00aab4fc) → [`00aab594`](#insn-00aab594)
- ブロック [`00aab500`](#insn-00aab500) 範囲 `[['00aab500', '00aab523']]`
  - `CONDITIONAL_JUMP` [`00aab520`](#insn-00aab520) → [`00aab594`](#insn-00aab594)
  - `FALL_THROUGH` [`00aab520`](#insn-00aab520) → [`00aab524`](#insn-00aab524)
- ブロック [`00aab524`](#insn-00aab524) 範囲 `[['00aab524', '00aab53f']]`
  - `UNCONDITIONAL_JUMP` [`00aab53c`](#insn-00aab53c) → [`00aab548`](#insn-00aab548)
- ブロック [`00aab540`](#insn-00aab540) 範囲 `[['00aab540', '00aab547']]`
  - `CONDITIONAL_JUMP` [`00aab544`](#insn-00aab544) → [`00aab594`](#insn-00aab594)
  - `FALL_THROUGH` [`00aab544`](#insn-00aab544) → [`00aab548`](#insn-00aab548)
- ブロック [`00aab548`](#insn-00aab548) 範囲 `[['00aab548', '00aab553']]`
  - `CONDITIONAL_JUMP` [`00aab550`](#insn-00aab550) → [`00aab540`](#insn-00aab540)
  - `FALL_THROUGH` [`00aab550`](#insn-00aab550) → [`00aab554`](#insn-00aab554)
- ブロック [`00aab554`](#insn-00aab554) 範囲 `[['00aab554', '00aab55b']]`
  - `CONDITIONAL_JUMP` [`00aab558`](#insn-00aab558) → [`00aab56c`](#insn-00aab56c)
  - `FALL_THROUGH` [`00aab558`](#insn-00aab558) → [`00aab55c`](#insn-00aab55c)
- ブロック [`00aab55c`](#insn-00aab55c) 範囲 `[['00aab55c', '00aab563']]`
  - `UNCONDITIONAL_JUMP` [`00aab560`](#insn-00aab560) → [`00aab540`](#insn-00aab540)
- ブロック [`00aab564`](#insn-00aab564) 範囲 `[['00aab564', '00aab56b']]`
  - `CONDITIONAL_JUMP` [`00aab568`](#insn-00aab568) → [`00aab59c`](#insn-00aab59c)
  - `FALL_THROUGH` [`00aab568`](#insn-00aab568) → [`00aab56c`](#insn-00aab56c)
- ブロック [`00aab56c`](#insn-00aab56c) 範囲 `[['00aab56c', '00aab57b']]`
  - `CONDITIONAL_JUMP` [`00aab578`](#insn-00aab578) → [`00aab564`](#insn-00aab564)
  - `FALL_THROUGH` [`00aab578`](#insn-00aab578) → [`00aab57c`](#insn-00aab57c)
- ブロック [`00aab57c`](#insn-00aab57c) 範囲 `[['00aab57c', '00aab583']]`
  - `CONDITIONAL_JUMP` [`00aab580`](#insn-00aab580) → [`00aab5f4`](#insn-00aab5f4)
  - `FALL_THROUGH` [`00aab580`](#insn-00aab580) → [`00aab584`](#insn-00aab584)
- ブロック [`00aab584`](#insn-00aab584) 範囲 `[['00aab584', '00aab58b']]`
  - `CONDITIONAL_JUMP` [`00aab588`](#insn-00aab588) → [`00aab56c`](#insn-00aab56c)
  - `FALL_THROUGH` [`00aab588`](#insn-00aab588) → [`00aab58c`](#insn-00aab58c)
- ブロック [`00aab58c`](#insn-00aab58c) 範囲 `[['00aab58c', '00aab593']]`
  - `UNCONDITIONAL_JUMP` [`00aab590`](#insn-00aab590) → [`00aab5a0`](#insn-00aab5a0)
- ブロック [`00aab594`](#insn-00aab594) 範囲 `[['00aab594', '00aab59b']]`
  - `UNCONDITIONAL_JUMP` [`00aab598`](#insn-00aab598) → [`00aab610`](#insn-00aab610)
- ブロック [`00aab59c`](#insn-00aab59c) 範囲 `[['00aab59c', '00aab59f']]`
  - `FALL_THROUGH` [`00aab59c`](#insn-00aab59c) → [`00aab5a0`](#insn-00aab5a0)
- ブロック [`00aab5a0`](#insn-00aab5a0) 範囲 `[['00aab5a0', '00aab5d3']]`
  - `CONDITIONAL_JUMP` [`00aab5d0`](#insn-00aab5d0) → [`00aab5dc`](#insn-00aab5dc)
  - `FALL_THROUGH` [`00aab5d0`](#insn-00aab5d0) → [`00aab5d4`](#insn-00aab5d4)
- ブロック [`00aab5d4`](#insn-00aab5d4) 範囲 `[['00aab5d4', '00aab5db']]`
  - `FALL_THROUGH` [`00aab5d8`](#insn-00aab5d8) → [`00aab5dc`](#insn-00aab5dc)
- ブロック [`00aab5dc`](#insn-00aab5dc) 範囲 `[['00aab5dc', '00aab5f3']]`
  - `UNCONDITIONAL_JUMP` [`00aab5f0`](#insn-00aab5f0) → [`00aab5f8`](#insn-00aab5f8)
- ブロック [`00aab5f4`](#insn-00aab5f4) 範囲 `[['00aab5f4', '00aab5f7']]`
  - `FALL_THROUGH` [`00aab5f4`](#insn-00aab5f4) → [`00aab5f8`](#insn-00aab5f8)
- ブロック [`00aab5f8`](#insn-00aab5f8) 範囲 `[['00aab5f8', '00aab60f']]`
  - `FALL_THROUGH` [`00aab60c`](#insn-00aab60c) → [`00aab610`](#insn-00aab610)
- ブロック [`00aab610`](#insn-00aab610) 範囲 `[['00aab610', '00aab623']]`

## 命令位置別の参照

- [`00aab4cc`](#insn-00aab4cc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab4d0`](#insn-00aab4d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab4d4`](#insn-00aab4d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab4d8`](#insn-00aab4d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab4f0`](#insn-00aab4f0) → [`00aab500`](#insn-00aab500) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab4f8`](#insn-00aab4f8) → [`00aab524`](#insn-00aab524) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab4fc`](#insn-00aab4fc) → [`00aab594`](#insn-00aab594) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab504`](#insn-00aab504) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aab50c`](#insn-00aab50c) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aab514`](#insn-00aab514) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aab520`](#insn-00aab520) → [`00aab594`](#insn-00aab594) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab53c`](#insn-00aab53c) → [`00aab548`](#insn-00aab548) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab544`](#insn-00aab544) → [`00aab594`](#insn-00aab594) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab550`](#insn-00aab550) → [`00aab540`](#insn-00aab540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab558`](#insn-00aab558) → [`00aab56c`](#insn-00aab56c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab560`](#insn-00aab560) → [`00aab540`](#insn-00aab540) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab568`](#insn-00aab568) → [`00aab59c`](#insn-00aab59c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab578`](#insn-00aab578) → [`00aab564`](#insn-00aab564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab580`](#insn-00aab580) → [`00aab5f4`](#insn-00aab5f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab588`](#insn-00aab588) → [`00aab56c`](#insn-00aab56c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab590`](#insn-00aab590) → [`00aab5a0`](#insn-00aab5a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab598`](#insn-00aab598) → [`00aab610`](#insn-00aab610) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab5a4`](#insn-00aab5a4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aab5d0`](#insn-00aab5d0) → [`00aab5dc`](#insn-00aab5dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab5e0`](#insn-00aab5e0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab5f0`](#insn-00aab5f0) → [`00aab5f8`](#insn-00aab5f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab610`](#insn-00aab610) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab614`](#insn-00aab614) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab618`](#insn-00aab618) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab61c`](#insn-00aab61c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aab4cc`](#insn-00aab4cc)

~~~json
{
  "source": "00aab4cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab4d0`](#insn-00aab4d0)

~~~json
{
  "source": "00aab4d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab4d4`](#insn-00aab4d4)

~~~json
{
  "source": "00aab4d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab4d8`](#insn-00aab4d8)

~~~json
{
  "source": "00aab4d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab4f0`](#insn-00aab4f0)

~~~json
{
  "source": "00aab4f0",
  "target": "00aab500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab4f8`](#insn-00aab4f8)

~~~json
{
  "source": "00aab4f8",
  "target": "00aab524",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab4fc`](#insn-00aab4fc)

~~~json
{
  "source": "00aab4fc",
  "target": "00aab594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab504`](#insn-00aab504)

~~~json
{
  "source": "00aab504",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab50c`](#insn-00aab50c)

~~~json
{
  "source": "00aab50c",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab514`](#insn-00aab514)

~~~json
{
  "source": "00aab514",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab520`](#insn-00aab520)

~~~json
{
  "source": "00aab520",
  "target": "00aab594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab53c`](#insn-00aab53c)

~~~json
{
  "source": "00aab53c",
  "target": "00aab548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab544`](#insn-00aab544)

~~~json
{
  "source": "00aab544",
  "target": "00aab594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab550`](#insn-00aab550)

~~~json
{
  "source": "00aab550",
  "target": "00aab540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab558`](#insn-00aab558)

~~~json
{
  "source": "00aab558",
  "target": "00aab56c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab560`](#insn-00aab560)

~~~json
{
  "source": "00aab560",
  "target": "00aab540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab568`](#insn-00aab568)

~~~json
{
  "source": "00aab568",
  "target": "00aab59c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab578`](#insn-00aab578)

~~~json
{
  "source": "00aab578",
  "target": "00aab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab580`](#insn-00aab580)

~~~json
{
  "source": "00aab580",
  "target": "00aab5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab588`](#insn-00aab588)

~~~json
{
  "source": "00aab588",
  "target": "00aab56c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab590`](#insn-00aab590)

~~~json
{
  "source": "00aab590",
  "target": "00aab5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab598`](#insn-00aab598)

~~~json
{
  "source": "00aab598",
  "target": "00aab610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab5a4`](#insn-00aab5a4)

~~~json
{
  "source": "00aab5a4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab5d0`](#insn-00aab5d0)

~~~json
{
  "source": "00aab5d0",
  "target": "00aab5dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab5e0`](#insn-00aab5e0)

~~~json
{
  "source": "00aab5e0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab5f0`](#insn-00aab5f0)

~~~json
{
  "source": "00aab5f0",
  "target": "00aab5f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab610`](#insn-00aab610)

~~~json
{
  "source": "00aab610",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab614`](#insn-00aab614)

~~~json
{
  "source": "00aab614",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab618`](#insn-00aab618)

~~~json
{
  "source": "00aab618",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab61c`](#insn-00aab61c)

~~~json
{
  "source": "00aab61c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
