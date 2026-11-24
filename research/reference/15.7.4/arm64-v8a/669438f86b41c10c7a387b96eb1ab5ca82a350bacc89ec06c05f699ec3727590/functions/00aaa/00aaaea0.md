# 00aaaea0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaae5c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-a354d393ebf3248c4b02fbe9c3566575)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0089.md#review-fc996f6c8c426995534c7695313d1154)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaaea0",
  "name": "FUN_00aaaea0",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02399844d3cc14da89562dd5da46bd3f82a6fceb8c31005e5a16757316d74e99",
  "source_text_sha256": "02399844d3cc14da89562dd5da46bd3f82a6fceb8c31005e5a16757316d74e99",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaaea0",
        "00aaafe7"
      ]
    ],
    "bytes_sha256": "a22c0f6fa31e3d2df63514953dfdf3100e667b7d2465b90c0c632a6bf7915ac2",
    "instruction_count": 82,
    "instruction_bytes": 328,
    "body_bytes": 328,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0079bdf0](../0079b/0079bdf0.md)
- [00a7268c](../00a72/00a7268c.md)

## 呼び出し先

- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aaa700](../00aaa/00aaa700.md)
- [00bdb600](../00bdb/00bdb600.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1823 bytes

~~~c

undefined8 FUN_00aaaea0(long param_1,ulong param_2,ulong param_3,ulong param_4)

{
  long lVar1;
  wchar_t *pwVar2;
  long lVar3;
  wchar_t *pwVar4;
  long lVar5;
  
  if ((int)param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_2 = param_2 & 0xffffffff;
    param_3 = FUN_007cfaa0();
    param_3 = param_3 & 0xffffffff;
    param_4 = FUN_007cfcd8();
    param_4 = param_4 & 0xffffffff;
  }
  FUN_00aaa700(param_1,param_2,param_3,param_4);
  lVar5 = 0;
  while( true ) {
    lVar3 = FUN_0081f580();
    lVar1 = lVar3 + lVar5;
    if (((uint)(*(byte *)(lVar3 + 0xc76e) ^ *(byte *)(lVar1 + 0xc746)) << 0x10 |
         (uint)(*(byte *)(lVar3 + 0xc76f) ^ *(byte *)(lVar1 + 0xc747)) << 0x18 |
         (uint)(*(byte *)(lVar3 + 0xc76d) ^ *(byte *)(lVar1 + 0xc745)) << 8 |
        (uint)(*(byte *)(lVar3 + 0xc76c) ^ *(byte *)(lVar1 + 0xc744))) == 0xffffffff) {
      return 0;
    }
    lVar3 = FUN_0081f580();
    lVar1 = lVar3 + lVar5;
    pwVar2 = *(wchar_t **)(param_1 + 0x38);
    pwVar4 = wmemchr(*(wchar_t **)(param_1 + 0x30),
                     CONCAT13(*(byte *)(lVar3 + 0xc76f) ^ *(byte *)(lVar1 + 0xc747),
                              CONCAT12(*(byte *)(lVar3 + 0xc76e) ^ *(byte *)(lVar1 + 0xc746),
                                       CONCAT11(*(byte *)(lVar3 + 0xc76d) ^
                                                *(byte *)(lVar1 + 0xc745),
                                                *(byte *)(lVar3 + 0xc76c) ^
                                                *(byte *)(lVar1 + 0xc744)))) + L'\xfffffffe',
                     (long)pwVar2 - (long)*(wchar_t **)(param_1 + 0x30) >> 2);
    if (pwVar4 != (wchar_t *)0x0) {
      pwVar2 = pwVar4;
    }
    if (pwVar2 != *(wchar_t **)(param_1 + 0x38)) break;
    lVar5 = lVar5 + 4;
    if (lVar5 == 0x28) {
      return 0;
    }
  }
  return 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaaea0"></a> `00aaaea0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aaaea4"></a> `00aaaea4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaaea8"></a> `00aaaea8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaaeac"></a> `00aaaeac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaaeb0"></a> `00aaaeb0` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaaeb4"></a> `00aaaeb4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaaeb8"></a> `00aaaeb8` | `41 01 00 54` | b.ne 0x00aaaee0 | `CONDITIONAL_JUMP`
<a id="insn-00aaaebc"></a> `00aaaebc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaaec0"></a> `00aaaec0` | `a4 92 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaec4"></a> `00aaaec4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aaaec8"></a> `00aaaec8` | `f6 92 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaecc"></a> `00aaaecc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaaed0"></a> `00aaaed0` | `82 93 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaed4"></a> `00aaaed4` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aaaed8"></a> `00aaaed8` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aaaedc"></a> `00aaaedc` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aaaee0"></a> `00aaaee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaaee4"></a> `00aaaee4` | `07 fe ff 97` | bl 0x00aaa700 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaee8"></a> `00aaaee8` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00aaaeec"></a> `00aaaeec` | `b5 e8 98 52` | mov w21,#0xc745 | `FALL_THROUGH`
<a id="insn-00aaaef0"></a> `00aaaef0` | `a4 d1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaef4"></a> `00aaaef4` | `08 00 14 8b` | add x8,x0,x20 | `FALL_THROUGH`
<a id="insn-00aaaef8"></a> `00aaaef8` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aaaefc"></a> `00aaaefc` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00aaaf00"></a> `00aaaf00` | `2b b9 5d 39` | ldrb w11,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aaaf04"></a> `00aaaf04` | `2c bd 5d 39` | ldrb w12,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aaaf08"></a> `00aaaf08` | `0a 05 40 39` | ldrb w10,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aaaf0c"></a> `00aaaf0c` | `0d 01 40 39` | ldrb w13,[x8] | `FALL_THROUGH`
<a id="insn-00aaaf10"></a> `00aaaf10` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aaaf14"></a> `00aaaf14` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aaaf18"></a> `00aaaf18` | `08 f1 5f 38` | ldurb w8,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00aaaf1c"></a> `00aaaf1c` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aaaf20"></a> `00aaaf20` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aaaf24"></a> `00aaaf24` | `2c b5 5d 39` | ldrb w12,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aaaf28"></a> `00aaaf28` | `29 b1 5d 39` | ldrb w9,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aaaf2c"></a> `00aaaf2c` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aaaf30"></a> `00aaaf30` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aaaf34"></a> `00aaaf34` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aaaf38"></a> `00aaaf38` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aaaf3c"></a> `00aaaf3c` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aaaf40"></a> `00aaaf40` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaaf44"></a> `00aaaf44` | `40 04 00 54` | b.eq 0x00aaafcc | `CONDITIONAL_JUMP`
<a id="insn-00aaaf48"></a> `00aaaf48` | `8e d1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaf4c"></a> `00aaaf4c` | `09 00 14 8b` | add x9,x0,x20 | `FALL_THROUGH`
<a id="insn-00aaaf50"></a> `00aaaf50` | `0a 30 40 91` | add x10,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aaaf54"></a> `00aaaf54` | `29 01 15 8b` | add x9,x9,x21 | `FALL_THROUGH`
<a id="insn-00aaaf58"></a> `00aaaf58` | `4b b1 5d 39` | ldrb w11,[x10, #0x76c] | `FALL_THROUGH`
<a id="insn-00aaaf5c"></a> `00aaaf5c` | `4d b5 5d 39` | ldrb w13,[x10, #0x76d] | `FALL_THROUGH`
<a id="insn-00aaaf60"></a> `00aaaf60` | `2c f1 5f 38` | ldurb w12,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00aaaf64"></a> `00aaaf64` | `2e 01 40 39` | ldrb w14,[x9] | `FALL_THROUGH`
<a id="insn-00aaaf68"></a> `00aaaf68` | `68 5a 43 a9` | ldp x8,x22,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aaaf6c"></a> `00aaaf6c` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00aaaf70"></a> `00aaaf70` | `ac 01 0e 4a` | eor w12,w13,w14 | `FALL_THROUGH`
<a id="insn-00aaaf74"></a> `00aaaf74` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00aaaf78"></a> `00aaaf78` | `4e b9 5d 39` | ldrb w14,[x10, #0x76e] | `FALL_THROUGH`
<a id="insn-00aaaf7c"></a> `00aaaf7c` | `6b 21 0c 2a` | orr w11,w11,w12, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aaaf80"></a> `00aaaf80` | `29 09 40 39` | ldrb w9,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00aaaf84"></a> `00aaaf84` | `4a bd 5d 39` | ldrb w10,[x10, #0x76f] | `FALL_THROUGH`
<a id="insn-00aaaf88"></a> `00aaaf88` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aaaf8c"></a> `00aaaf8c` | `cc 01 0d 4a` | eor w12,w14,w13 | `FALL_THROUGH`
<a id="insn-00aaaf90"></a> `00aaaf90` | `6b 41 0c 2a` | orr w11,w11,w12, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aaaf94"></a> `00aaaf94` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00aaaf98"></a> `00aaaf98` | `ca 02 08 cb` | sub x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00aaaf9c"></a> `00aaaf9c` | `42 fd 42 93` | asr x2,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00aaafa0"></a> `00aaafa0` | `69 61 09 2a` | orr w9,w11,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aaafa4"></a> `00aaafa4` | `21 09 00 51` | sub w1,w9,#0x2 | `FALL_THROUGH`
<a id="insn-00aaafa8"></a> `00aaafa8` | `96 c1 04 94` | bl 0x00bdb600 | `UNCONDITIONAL_CALL`
<a id="insn-00aaafac"></a> `00aaafac` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00aaafb0"></a> `00aaafb0` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaafb4"></a> `00aaafb4` | `c9 02 80 9a` | csel x9,x22,x0,eq | `FALL_THROUGH`
<a id="insn-00aaafb8"></a> `00aaafb8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aaafbc"></a> `00aaafbc` | `c1 00 00 54` | b.ne 0x00aaafd4 | `CONDITIONAL_JUMP`
<a id="insn-00aaafc0"></a> `00aaafc0` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00aaafc4"></a> `00aaafc4` | `9f a2 00 f1` | cmp x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aaafc8"></a> `00aaafc8` | `41 f9 ff 54` | b.ne 0x00aaaef0 | `CONDITIONAL_JUMP`
<a id="insn-00aaafcc"></a> `00aaafcc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaafd0"></a> `00aaafd0` | `02 00 00 14` | b 0x00aaafd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaafd4"></a> `00aaafd4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aaafd8"></a> `00aaafd8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaafdc"></a> `00aaafdc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaafe0"></a> `00aaafe0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aaafe4"></a> `00aaafe4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaaea0`](#insn-00aaaea0) 範囲 `[['00aaaea0', '00aaaebb']]`
  - `CONDITIONAL_JUMP` [`00aaaeb8`](#insn-00aaaeb8) → [`00aaaee0`](#insn-00aaaee0)
  - `FALL_THROUGH` [`00aaaeb8`](#insn-00aaaeb8) → [`00aaaebc`](#insn-00aaaebc)
- ブロック [`00aaaebc`](#insn-00aaaebc) 範囲 `[['00aaaebc', '00aaaedf']]`
  - `FALL_THROUGH` [`00aaaedc`](#insn-00aaaedc) → [`00aaaee0`](#insn-00aaaee0)
- ブロック [`00aaaee0`](#insn-00aaaee0) 範囲 `[['00aaaee0', '00aaaeef']]`
  - `FALL_THROUGH` [`00aaaeec`](#insn-00aaaeec) → [`00aaaef0`](#insn-00aaaef0)
- ブロック [`00aaaef0`](#insn-00aaaef0) 範囲 `[['00aaaef0', '00aaaf47']]`
  - `CONDITIONAL_JUMP` [`00aaaf44`](#insn-00aaaf44) → [`00aaafcc`](#insn-00aaafcc)
  - `FALL_THROUGH` [`00aaaf44`](#insn-00aaaf44) → [`00aaaf48`](#insn-00aaaf48)
- ブロック [`00aaaf48`](#insn-00aaaf48) 範囲 `[['00aaaf48', '00aaafbf']]`
  - `CONDITIONAL_JUMP` [`00aaafbc`](#insn-00aaafbc) → [`00aaafd4`](#insn-00aaafd4)
  - `FALL_THROUGH` [`00aaafbc`](#insn-00aaafbc) → [`00aaafc0`](#insn-00aaafc0)
- ブロック [`00aaafc0`](#insn-00aaafc0) 範囲 `[['00aaafc0', '00aaafcb']]`
  - `CONDITIONAL_JUMP` [`00aaafc8`](#insn-00aaafc8) → [`00aaaef0`](#insn-00aaaef0)
  - `FALL_THROUGH` [`00aaafc8`](#insn-00aaafc8) → [`00aaafcc`](#insn-00aaafcc)
- ブロック [`00aaafcc`](#insn-00aaafcc) 範囲 `[['00aaafcc', '00aaafd3']]`
  - `UNCONDITIONAL_JUMP` [`00aaafd0`](#insn-00aaafd0) → [`00aaafd8`](#insn-00aaafd8)
- ブロック [`00aaafd4`](#insn-00aaafd4) 範囲 `[['00aaafd4', '00aaafd7']]`
  - `FALL_THROUGH` [`00aaafd4`](#insn-00aaafd4) → [`00aaafd8`](#insn-00aaafd8)
- ブロック [`00aaafd8`](#insn-00aaafd8) 範囲 `[['00aaafd8', '00aaafe7']]`

## 命令位置別の参照

- [`00aaaea0`](#insn-00aaaea0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaea4`](#insn-00aaaea4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaea8`](#insn-00aaaea8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaeb8`](#insn-00aaaeb8) → [`00aaaee0`](#insn-00aaaee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaec0`](#insn-00aaaec0) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aaaec8`](#insn-00aaaec8) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aaaed0`](#insn-00aaaed0) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aaaee4`](#insn-00aaaee4) → [`00aaa700`](00aaa700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaa700` · 推定シンボル `None` · 推定型 `None`
- [`00aaaef0`](#insn-00aaaef0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf44`](#insn-00aaaf44) → [`00aaafcc`](#insn-00aaafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf48`](#insn-00aaaf48) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aaafa8`](#insn-00aaafa8) → [`00bdb600`](../00bdb/00bdb600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb600` · 推定シンボル `None` · 推定型 `None`
- [`00aaafbc`](#insn-00aaafbc) → [`00aaafd4`](#insn-00aaafd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafc8`](#insn-00aaafc8) → [`00aaaef0`](#insn-00aaaef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafd0`](#insn-00aaafd0) → [`00aaafd8`](#insn-00aaafd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafd8`](#insn-00aaafd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafdc`](#insn-00aaafdc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafe0`](#insn-00aaafe0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaaea0`](#insn-00aaaea0)

~~~json
{
  "source": "00aaaea0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaea4`](#insn-00aaaea4)

~~~json
{
  "source": "00aaaea4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaea8`](#insn-00aaaea8)

~~~json
{
  "source": "00aaaea8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaeb8`](#insn-00aaaeb8)

~~~json
{
  "source": "00aaaeb8",
  "target": "00aaaee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaec0`](#insn-00aaaec0)

~~~json
{
  "source": "00aaaec0",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaec8`](#insn-00aaaec8)

~~~json
{
  "source": "00aaaec8",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaed0`](#insn-00aaaed0)

~~~json
{
  "source": "00aaaed0",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaee4`](#insn-00aaaee4)

~~~json
{
  "source": "00aaaee4",
  "target": "00aaa700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaef0`](#insn-00aaaef0)

~~~json
{
  "source": "00aaaef0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf44`](#insn-00aaaf44)

~~~json
{
  "source": "00aaaf44",
  "target": "00aaafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf48`](#insn-00aaaf48)

~~~json
{
  "source": "00aaaf48",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaafa8`](#insn-00aaafa8)

~~~json
{
  "source": "00aaafa8",
  "target": "00bdb600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaafbc`](#insn-00aaafbc)

~~~json
{
  "source": "00aaafbc",
  "target": "00aaafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafc8`](#insn-00aaafc8)

~~~json
{
  "source": "00aaafc8",
  "target": "00aaaef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafd0`](#insn-00aaafd0)

~~~json
{
  "source": "00aaafd0",
  "target": "00aaafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafd8`](#insn-00aaafd8)

~~~json
{
  "source": "00aaafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafdc`](#insn-00aaafdc)

~~~json
{
  "source": "00aaafdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafe0`](#insn-00aaafe0)

~~~json
{
  "source": "00aaafe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
