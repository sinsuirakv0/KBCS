# 00aaae5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaad94`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-d48bc6efc042c3ee0fd168bc0dd52431)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaaea0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaaea0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-a354d393ebf3248c4b02fbe9c3566575)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaae5c",
  "name": "FUN_00aaae5c",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9de3ab0e60effabf0bfe5d87df3af35b7affd9262c87c4e0493cb9162c8d36d",
  "source_text_sha256": "e9de3ab0e60effabf0bfe5d87df3af35b7affd9262c87c4e0493cb9162c8d36d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaae5c",
        "00aaafa3"
      ]
    ],
    "bytes_sha256": "258342c4f9c886778bb680c95163ea8b99d1fdba51f580a8c061818eaf3fed77",
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
- [00a72648](../00a72/00a72648.md)

## 呼び出し先

- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aaa6bc](../00aaa/00aaa6bc.md)
- [00bdb5b0](../00bdb/00bdb5b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1823 bytes

~~~c

undefined8 FUN_00aaae5c(long param_1,ulong param_2,ulong param_3,ulong param_4)

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
  FUN_00aaa6bc(param_1,param_2,param_3,param_4);
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
<a id="insn-00aaae5c"></a> `00aaae5c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aaae60"></a> `00aaae60` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaae64"></a> `00aaae64` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaae68"></a> `00aaae68` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaae6c"></a> `00aaae6c` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaae70"></a> `00aaae70` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaae74"></a> `00aaae74` | `41 01 00 54` | b.ne 0x00aaae9c | `CONDITIONAL_JUMP`
<a id="insn-00aaae78"></a> `00aaae78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaae7c"></a> `00aaae7c` | `b5 92 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aaae80"></a> `00aaae80` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aaae84"></a> `00aaae84` | `07 93 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaae88"></a> `00aaae88` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaae8c"></a> `00aaae8c` | `93 93 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aaae90"></a> `00aaae90` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aaae94"></a> `00aaae94` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aaae98"></a> `00aaae98` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aaae9c"></a> `00aaae9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaaea0"></a> `00aaaea0` | `07 fe ff 97` | bl 0x00aaa6bc | `UNCONDITIONAL_CALL`
<a id="insn-00aaaea4"></a> `00aaaea4` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00aaaea8"></a> `00aaaea8` | `b5 e8 98 52` | mov w21,#0xc745 | `FALL_THROUGH`
<a id="insn-00aaaeac"></a> `00aaaeac` | `b5 d1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaeb0"></a> `00aaaeb0` | `08 00 14 8b` | add x8,x0,x20 | `FALL_THROUGH`
<a id="insn-00aaaeb4"></a> `00aaaeb4` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aaaeb8"></a> `00aaaeb8` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00aaaebc"></a> `00aaaebc` | `2b b9 5d 39` | ldrb w11,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aaaec0"></a> `00aaaec0` | `2c bd 5d 39` | ldrb w12,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aaaec4"></a> `00aaaec4` | `0a 05 40 39` | ldrb w10,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aaaec8"></a> `00aaaec8` | `0d 01 40 39` | ldrb w13,[x8] | `FALL_THROUGH`
<a id="insn-00aaaecc"></a> `00aaaecc` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aaaed0"></a> `00aaaed0` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aaaed4"></a> `00aaaed4` | `08 f1 5f 38` | ldurb w8,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00aaaed8"></a> `00aaaed8` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aaaedc"></a> `00aaaedc` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aaaee0"></a> `00aaaee0` | `2c b5 5d 39` | ldrb w12,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aaaee4"></a> `00aaaee4` | `29 b1 5d 39` | ldrb w9,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aaaee8"></a> `00aaaee8` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aaaeec"></a> `00aaaeec` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aaaef0"></a> `00aaaef0` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aaaef4"></a> `00aaaef4` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aaaef8"></a> `00aaaef8` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aaaefc"></a> `00aaaefc` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaaf00"></a> `00aaaf00` | `40 04 00 54` | b.eq 0x00aaaf88 | `CONDITIONAL_JUMP`
<a id="insn-00aaaf04"></a> `00aaaf04` | `9f d1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaf08"></a> `00aaaf08` | `09 00 14 8b` | add x9,x0,x20 | `FALL_THROUGH`
<a id="insn-00aaaf0c"></a> `00aaaf0c` | `0a 30 40 91` | add x10,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aaaf10"></a> `00aaaf10` | `29 01 15 8b` | add x9,x9,x21 | `FALL_THROUGH`
<a id="insn-00aaaf14"></a> `00aaaf14` | `4b b1 5d 39` | ldrb w11,[x10, #0x76c] | `FALL_THROUGH`
<a id="insn-00aaaf18"></a> `00aaaf18` | `4d b5 5d 39` | ldrb w13,[x10, #0x76d] | `FALL_THROUGH`
<a id="insn-00aaaf1c"></a> `00aaaf1c` | `2c f1 5f 38` | ldurb w12,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00aaaf20"></a> `00aaaf20` | `2e 01 40 39` | ldrb w14,[x9] | `FALL_THROUGH`
<a id="insn-00aaaf24"></a> `00aaaf24` | `68 5a 43 a9` | ldp x8,x22,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aaaf28"></a> `00aaaf28` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00aaaf2c"></a> `00aaaf2c` | `ac 01 0e 4a` | eor w12,w13,w14 | `FALL_THROUGH`
<a id="insn-00aaaf30"></a> `00aaaf30` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00aaaf34"></a> `00aaaf34` | `4e b9 5d 39` | ldrb w14,[x10, #0x76e] | `FALL_THROUGH`
<a id="insn-00aaaf38"></a> `00aaaf38` | `6b 21 0c 2a` | orr w11,w11,w12, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aaaf3c"></a> `00aaaf3c` | `29 09 40 39` | ldrb w9,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00aaaf40"></a> `00aaaf40` | `4a bd 5d 39` | ldrb w10,[x10, #0x76f] | `FALL_THROUGH`
<a id="insn-00aaaf44"></a> `00aaaf44` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aaaf48"></a> `00aaaf48` | `cc 01 0d 4a` | eor w12,w14,w13 | `FALL_THROUGH`
<a id="insn-00aaaf4c"></a> `00aaaf4c` | `6b 41 0c 2a` | orr w11,w11,w12, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aaaf50"></a> `00aaaf50` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00aaaf54"></a> `00aaaf54` | `ca 02 08 cb` | sub x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00aaaf58"></a> `00aaaf58` | `42 fd 42 93` | asr x2,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00aaaf5c"></a> `00aaaf5c` | `69 61 09 2a` | orr w9,w11,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aaaf60"></a> `00aaaf60` | `21 09 00 51` | sub w1,w9,#0x2 | `FALL_THROUGH`
<a id="insn-00aaaf64"></a> `00aaaf64` | `93 c1 04 94` | bl 0x00bdb5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaf68"></a> `00aaaf68` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00aaaf6c"></a> `00aaaf6c` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaaf70"></a> `00aaaf70` | `c9 02 80 9a` | csel x9,x22,x0,eq | `FALL_THROUGH`
<a id="insn-00aaaf74"></a> `00aaaf74` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aaaf78"></a> `00aaaf78` | `c1 00 00 54` | b.ne 0x00aaaf90 | `CONDITIONAL_JUMP`
<a id="insn-00aaaf7c"></a> `00aaaf7c` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00aaaf80"></a> `00aaaf80` | `9f a2 00 f1` | cmp x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aaaf84"></a> `00aaaf84` | `41 f9 ff 54` | b.ne 0x00aaaeac | `CONDITIONAL_JUMP`
<a id="insn-00aaaf88"></a> `00aaaf88` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaaf8c"></a> `00aaaf8c` | `02 00 00 14` | b 0x00aaaf94 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaaf90"></a> `00aaaf90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aaaf94"></a> `00aaaf94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaaf98"></a> `00aaaf98` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaaf9c"></a> `00aaaf9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aaafa0"></a> `00aaafa0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaae5c`](#insn-00aaae5c) 範囲 `[['00aaae5c', '00aaae77']]`
  - `CONDITIONAL_JUMP` [`00aaae74`](#insn-00aaae74) → [`00aaae9c`](#insn-00aaae9c)
  - `FALL_THROUGH` [`00aaae74`](#insn-00aaae74) → [`00aaae78`](#insn-00aaae78)
- ブロック [`00aaae78`](#insn-00aaae78) 範囲 `[['00aaae78', '00aaae9b']]`
  - `FALL_THROUGH` [`00aaae98`](#insn-00aaae98) → [`00aaae9c`](#insn-00aaae9c)
- ブロック [`00aaae9c`](#insn-00aaae9c) 範囲 `[['00aaae9c', '00aaaeab']]`
  - `FALL_THROUGH` [`00aaaea8`](#insn-00aaaea8) → [`00aaaeac`](#insn-00aaaeac)
- ブロック [`00aaaeac`](#insn-00aaaeac) 範囲 `[['00aaaeac', '00aaaf03']]`
  - `CONDITIONAL_JUMP` [`00aaaf00`](#insn-00aaaf00) → [`00aaaf88`](#insn-00aaaf88)
  - `FALL_THROUGH` [`00aaaf00`](#insn-00aaaf00) → [`00aaaf04`](#insn-00aaaf04)
- ブロック [`00aaaf04`](#insn-00aaaf04) 範囲 `[['00aaaf04', '00aaaf7b']]`
  - `CONDITIONAL_JUMP` [`00aaaf78`](#insn-00aaaf78) → [`00aaaf90`](#insn-00aaaf90)
  - `FALL_THROUGH` [`00aaaf78`](#insn-00aaaf78) → [`00aaaf7c`](#insn-00aaaf7c)
- ブロック [`00aaaf7c`](#insn-00aaaf7c) 範囲 `[['00aaaf7c', '00aaaf87']]`
  - `CONDITIONAL_JUMP` [`00aaaf84`](#insn-00aaaf84) → [`00aaaeac`](#insn-00aaaeac)
  - `FALL_THROUGH` [`00aaaf84`](#insn-00aaaf84) → [`00aaaf88`](#insn-00aaaf88)
- ブロック [`00aaaf88`](#insn-00aaaf88) 範囲 `[['00aaaf88', '00aaaf8f']]`
  - `UNCONDITIONAL_JUMP` [`00aaaf8c`](#insn-00aaaf8c) → [`00aaaf94`](#insn-00aaaf94)
- ブロック [`00aaaf90`](#insn-00aaaf90) 範囲 `[['00aaaf90', '00aaaf93']]`
  - `FALL_THROUGH` [`00aaaf90`](#insn-00aaaf90) → [`00aaaf94`](#insn-00aaaf94)
- ブロック [`00aaaf94`](#insn-00aaaf94) 範囲 `[['00aaaf94', '00aaafa3']]`

## 命令位置別の参照

- [`00aaae5c`](#insn-00aaae5c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaae60`](#insn-00aaae60) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaae64`](#insn-00aaae64) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaae74`](#insn-00aaae74) → [`00aaae9c`](#insn-00aaae9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaae7c`](#insn-00aaae7c) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aaae84`](#insn-00aaae84) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aaae8c`](#insn-00aaae8c) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aaaea0`](#insn-00aaaea0) → [`00aaa6bc`](00aaa6bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaa6bc` · 推定シンボル `None` · 推定型 `None`
- [`00aaaeac`](#insn-00aaaeac) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf00`](#insn-00aaaf00) → [`00aaaf88`](#insn-00aaaf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf04`](#insn-00aaaf04) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf64`](#insn-00aaaf64) → [`00bdb5b0`](../00bdb/00bdb5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb5b0` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf78`](#insn-00aaaf78) → [`00aaaf90`](#insn-00aaaf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf84`](#insn-00aaaf84) → [`00aaaeac`](#insn-00aaaeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf8c`](#insn-00aaaf8c) → [`00aaaf94`](#insn-00aaaf94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf94`](#insn-00aaaf94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf98`](#insn-00aaaf98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf9c`](#insn-00aaaf9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaae5c`](#insn-00aaae5c)

~~~json
{
  "source": "00aaae5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaae60`](#insn-00aaae60)

~~~json
{
  "source": "00aaae60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaae64`](#insn-00aaae64)

~~~json
{
  "source": "00aaae64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaae74`](#insn-00aaae74)

~~~json
{
  "source": "00aaae74",
  "target": "00aaae9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaae7c`](#insn-00aaae7c)

~~~json
{
  "source": "00aaae7c",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaae84`](#insn-00aaae84)

~~~json
{
  "source": "00aaae84",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaae8c`](#insn-00aaae8c)

~~~json
{
  "source": "00aaae8c",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaea0`](#insn-00aaaea0)

~~~json
{
  "source": "00aaaea0",
  "target": "00aaa6bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaeac`](#insn-00aaaeac)

~~~json
{
  "source": "00aaaeac",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf00`](#insn-00aaaf00)

~~~json
{
  "source": "00aaaf00",
  "target": "00aaaf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf04`](#insn-00aaaf04)

~~~json
{
  "source": "00aaaf04",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf64`](#insn-00aaaf64)

~~~json
{
  "source": "00aaaf64",
  "target": "00bdb5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf78`](#insn-00aaaf78)

~~~json
{
  "source": "00aaaf78",
  "target": "00aaaf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf84`](#insn-00aaaf84)

~~~json
{
  "source": "00aaaf84",
  "target": "00aaaeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf8c`](#insn-00aaaf8c)

~~~json
{
  "source": "00aaaf8c",
  "target": "00aaaf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf94`](#insn-00aaaf94)

~~~json
{
  "source": "00aaaf94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf98`](#insn-00aaaf98)

~~~json
{
  "source": "00aaaf98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf9c`](#insn-00aaaf9c)

~~~json
{
  "source": "00aaaf9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
