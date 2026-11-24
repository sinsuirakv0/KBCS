# 00a3afcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3af88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0002.md#compare-732af37ee8b1181e548d64e0e62c6b81)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0078.md#review-4109fdcfe5c3f31a6e07c5a81c060e6e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3afcc",
  "name": "FUN_00a3afcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "829eb6052f200d360cb03d6b74bc588646bf0da024afb7e5db00f7285fb96047",
  "source_text_sha256": "829eb6052f200d360cb03d6b74bc588646bf0da024afb7e5db00f7285fb96047",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3afcc",
        "00a3b0cf"
      ]
    ],
    "bytes_sha256": "f0480a3c1f8fe2ab22ebbbfa617c874f5692f9869d5be3079bad1866538c8b93",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041c8f8](../0041c/0041c8f8.md)
- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00883cc0](../00883/00883cc0.md)
- [009e97e4](../009e9/009e97e4.md)
- [009e97fc](../009e9/009e97fc.md)
- [009ea92c](../009ea/009ea92c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1107 bytes

~~~c

void FUN_00a3afcc(long param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  uint uVar2;
  int iVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long lVar6;
  
  uVar5 = *param_2;
  iVar3 = *param_3;
  lVar6 = *(long *)(param_1 + 8);
  uVar4 = FUN_00883cc0(uVar5);
  uVar4 = FUN_009e97fc(uVar4,1);
  if (iVar3 == 2) {
    iVar3 = *(int *)(BYTE_ARRAY_0032ff39 + lVar6 + 0x23);
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    uVar1 = iVar3 >> 1 & 1;
    uVar2 = -uVar1;
    if (-1 < iVar3 >> 1) {
      uVar2 = uVar1;
    }
    FUN_009ea92c(uVar4,uVar2 + 2,uVar2 + 9);
    uVar4 = FUN_00883cc0(uVar5);
    uVar4 = FUN_009e97fc(uVar4,1);
    FUN_009e97e4(uVar4,1);
    return;
  }
  FUN_009e97e4(uVar4,0);
  if (iVar3 != 4) {
    if (iVar3 == 3) {
      uVar4 = FUN_00457e1c();
      uVar5 = 0xb;
    }
    else {
      if (iVar3 != 0) {
        return;
      }
      uVar4 = FUN_00457e1c();
      uVar5 = 10;
    }
    FUN_00459efc(uVar4,uVar5,0);
    return;
  }
  *(undefined4 *)(lVar6 + 0x3388) = 0x21;
  *(undefined1 *)(lVar6 + 0x3390) = 1;
  FUN_0041be0c();
  FUN_0041c8f8();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3afcc"></a> `00a3afcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a3afd0"></a> `00a3afd0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3afd4"></a> `00a3afd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3afd8"></a> `00a3afd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3afdc"></a> `00a3afdc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00a3afe0"></a> `00a3afe0` | `55 00 40 b9` | ldr w21,[x2] | `FALL_THROUGH`
<a id="insn-00a3afe4"></a> `00a3afe4` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a3afe8"></a> `00a3afe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3afec"></a> `00a3afec` | `35 23 f9 97` | bl 0x00883cc0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3aff0"></a> `00a3aff0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00a3aff4"></a> `00a3aff4` | `02 ba fe 97` | bl 0x009e97fc | `UNCONDITIONAL_CALL`
<a id="insn-00a3aff8"></a> `00a3aff8` | `bf 0a 00 71` | cmp w21,#0x2 | `FALL_THROUGH`
<a id="insn-00a3affc"></a> `00a3affc` | `c1 02 00 54` | b.ne 0x00a3b054 | `CONDITIONAL_JUMP`
<a id="insn-00a3b000"></a> `00a3b000` | `88 eb 9f 52` | mov w8,#0xff5c | `FALL_THROUGH`
<a id="insn-00a3b004"></a> `00a3b004` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3b008"></a> `00a3b008` | `88 6a 68 b8` | ldr w8,[x20, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3b00c"></a> `00a3b00c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00a3b010"></a> `00a3b010` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00a3b014"></a> `00a3b014` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a3b018"></a> `00a3b018` | `09 01 00 12` | and w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a3b01c"></a> `00a3b01c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00a3b020"></a> `00a3b020` | `28 a5 89 5a` | cneg w8,w9,lt | `FALL_THROUGH`
<a id="insn-00a3b024"></a> `00a3b024` | `01 09 00 11` | add w1,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a3b028"></a> `00a3b028` | `02 25 00 11` | add w2,w8,#0x9 | `FALL_THROUGH`
<a id="insn-00a3b02c"></a> `00a3b02c` | `40 be fe 97` | bl 0x009ea92c | `UNCONDITIONAL_CALL`
<a id="insn-00a3b030"></a> `00a3b030` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3b034"></a> `00a3b034` | `23 23 f9 97` | bl 0x00883cc0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3b038"></a> `00a3b038` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00a3b03c"></a> `00a3b03c` | `f0 b9 fe 97` | bl 0x009e97fc | `UNCONDITIONAL_CALL`
<a id="insn-00a3b040"></a> `00a3b040` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00a3b044"></a> `00a3b044` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3b048"></a> `00a3b048` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3b04c"></a> `00a3b04c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3b050"></a> `00a3b050` | `e5 b9 fe 17` | b 0x009e97e4 | `CALL_TERMINATOR`
<a id="insn-00a3b054"></a> `00a3b054` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a3b058"></a> `00a3b058` | `e3 b9 fe 97` | bl 0x009e97e4 | `UNCONDITIONAL_CALL`
<a id="insn-00a3b05c"></a> `00a3b05c` | `bf 12 00 71` | cmp w21,#0x4 | `FALL_THROUGH`
<a id="insn-00a3b060"></a> `00a3b060` | `c0 01 00 54` | b.eq 0x00a3b098 | `CONDITIONAL_JUMP`
<a id="insn-00a3b064"></a> `00a3b064` | `bf 0e 00 71` | cmp w21,#0x3 | `FALL_THROUGH`
<a id="insn-00a3b068"></a> `00a3b068` | `a0 00 00 54` | b.eq 0x00a3b07c | `CONDITIONAL_JUMP`
<a id="insn-00a3b06c"></a> `00a3b06c` | `b5 02 00 35` | cbnz w21,0x00a3b0c0 | `CONDITIONAL_JUMP`
<a id="insn-00a3b070"></a> `00a3b070` | `6b 73 e8 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a3b074"></a> `00a3b074` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00a3b078"></a> `00a3b078` | `03 00 00 14` | b 0x00a3b084 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3b07c"></a> `00a3b07c` | `68 73 e8 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a3b080"></a> `00a3b080` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00a3b084"></a> `00a3b084` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00a3b088"></a> `00a3b088` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3b08c"></a> `00a3b08c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3b090"></a> `00a3b090` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3b094"></a> `00a3b094` | `9a 7b e8 17` | b 0x00459efc | `CALL_TERMINATOR`
<a id="insn-00a3b098"></a> `00a3b098` | `28 04 80 52` | mov w8,#0x21 | `FALL_THROUGH`
<a id="insn-00a3b09c"></a> `00a3b09c` | `09 72 86 52` | mov w9,#0x3390 | `FALL_THROUGH`
<a id="insn-00a3b0a0"></a> `00a3b0a0` | `88 8a 33 b9` | str w8,[x20, #0x3388] | `FALL_THROUGH`
<a id="insn-00a3b0a4"></a> `00a3b0a4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a3b0a8"></a> `00a3b0a8` | `88 6a 29 38` | strb w8,[x20, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00a3b0ac"></a> `00a3b0ac` | `58 83 e7 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00a3b0b0"></a> `00a3b0b0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3b0b4"></a> `00a3b0b4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3b0b8"></a> `00a3b0b8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3b0bc"></a> `00a3b0bc` | `0f 86 e7 17` | b 0x0041c8f8 | `CALL_TERMINATOR`
<a id="insn-00a3b0c0"></a> `00a3b0c0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3b0c4"></a> `00a3b0c4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3b0c8"></a> `00a3b0c8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3b0cc"></a> `00a3b0cc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3afcc`](#insn-00a3afcc) 範囲 `[['00a3afcc', '00a3afff']]`
  - `CONDITIONAL_JUMP` [`00a3affc`](#insn-00a3affc) → [`00a3b054`](#insn-00a3b054)
  - `FALL_THROUGH` [`00a3affc`](#insn-00a3affc) → [`00a3b000`](#insn-00a3b000)
- ブロック [`00a3b000`](#insn-00a3b000) 範囲 `[['00a3b000', '00a3b053']]`
- ブロック [`00a3b054`](#insn-00a3b054) 範囲 `[['00a3b054', '00a3b063']]`
  - `CONDITIONAL_JUMP` [`00a3b060`](#insn-00a3b060) → [`00a3b098`](#insn-00a3b098)
  - `FALL_THROUGH` [`00a3b060`](#insn-00a3b060) → [`00a3b064`](#insn-00a3b064)
- ブロック [`00a3b064`](#insn-00a3b064) 範囲 `[['00a3b064', '00a3b06b']]`
  - `CONDITIONAL_JUMP` [`00a3b068`](#insn-00a3b068) → [`00a3b07c`](#insn-00a3b07c)
  - `FALL_THROUGH` [`00a3b068`](#insn-00a3b068) → [`00a3b06c`](#insn-00a3b06c)
- ブロック [`00a3b06c`](#insn-00a3b06c) 範囲 `[['00a3b06c', '00a3b06f']]`
  - `CONDITIONAL_JUMP` [`00a3b06c`](#insn-00a3b06c) → [`00a3b0c0`](#insn-00a3b0c0)
  - `FALL_THROUGH` [`00a3b06c`](#insn-00a3b06c) → [`00a3b070`](#insn-00a3b070)
- ブロック [`00a3b070`](#insn-00a3b070) 範囲 `[['00a3b070', '00a3b07b']]`
  - `UNCONDITIONAL_JUMP` [`00a3b078`](#insn-00a3b078) → [`00a3b084`](#insn-00a3b084)
- ブロック [`00a3b07c`](#insn-00a3b07c) 範囲 `[['00a3b07c', '00a3b083']]`
  - `FALL_THROUGH` [`00a3b080`](#insn-00a3b080) → [`00a3b084`](#insn-00a3b084)
- ブロック [`00a3b084`](#insn-00a3b084) 範囲 `[['00a3b084', '00a3b097']]`
- ブロック [`00a3b098`](#insn-00a3b098) 範囲 `[['00a3b098', '00a3b0bf']]`
- ブロック [`00a3b0c0`](#insn-00a3b0c0) 範囲 `[['00a3b0c0', '00a3b0cf']]`

## 命令位置別の参照

- [`00a3afcc`](#insn-00a3afcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3afd0`](#insn-00a3afd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3afd4`](#insn-00a3afd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3afec`](#insn-00a3afec) → [`00883cc0`](../00883/00883cc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883cc0` · 推定シンボル `None` · 推定型 `None`
- [`00a3aff4`](#insn-00a3aff4) → [`009e97fc`](../009e9/009e97fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e97fc` · 推定シンボル `None` · 推定型 `None`
- [`00a3affc`](#insn-00a3affc) → [`00a3b054`](#insn-00a3b054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b008`](#insn-00a3b008) → `0032ff5c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00a3b02c`](#insn-00a3b02c) → [`009ea92c`](../009ea/009ea92c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009ea92c` · 推定シンボル `None` · 推定型 `None`
- [`00a3b034`](#insn-00a3b034) → [`00883cc0`](../00883/00883cc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883cc0` · 推定シンボル `None` · 推定型 `None`
- [`00a3b03c`](#insn-00a3b03c) → [`009e97fc`](../009e9/009e97fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e97fc` · 推定シンボル `None` · 推定型 `None`
- [`00a3b044`](#insn-00a3b044) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b048`](#insn-00a3b048) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b04c`](#insn-00a3b04c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b050`](#insn-00a3b050) → [`009e97e4`](../009e9/009e97e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e97e4` · 推定シンボル `None` · 推定型 `None`
- [`00a3b058`](#insn-00a3b058) → [`009e97e4`](../009e9/009e97e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e97e4` · 推定シンボル `None` · 推定型 `None`
- [`00a3b060`](#insn-00a3b060) → [`00a3b098`](#insn-00a3b098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b068`](#insn-00a3b068) → [`00a3b07c`](#insn-00a3b07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b06c`](#insn-00a3b06c) → [`00a3b0c0`](#insn-00a3b0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b070`](#insn-00a3b070) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a3b078`](#insn-00a3b078) → [`00a3b084`](#insn-00a3b084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b07c`](#insn-00a3b07c) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a3b088`](#insn-00a3b088) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b08c`](#insn-00a3b08c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b090`](#insn-00a3b090) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b094`](#insn-00a3b094) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0ac`](#insn-00a3b0ac) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0b0`](#insn-00a3b0b0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0b4`](#insn-00a3b0b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0b8`](#insn-00a3b0b8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0bc`](#insn-00a3b0bc) → [`0041c8f8`](../0041c/0041c8f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041c8f8` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0c0`](#insn-00a3b0c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0c4`](#insn-00a3b0c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3b0c8`](#insn-00a3b0c8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3afcc`](#insn-00a3afcc)

~~~json
{
  "source": "00a3afcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3afd0`](#insn-00a3afd0)

~~~json
{
  "source": "00a3afd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3afd4`](#insn-00a3afd4)

~~~json
{
  "source": "00a3afd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3afec`](#insn-00a3afec)

~~~json
{
  "source": "00a3afec",
  "target": "00883cc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3aff4`](#insn-00a3aff4)

~~~json
{
  "source": "00a3aff4",
  "target": "009e97fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3affc`](#insn-00a3affc)

~~~json
{
  "source": "00a3affc",
  "target": "00a3b054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b008`](#insn-00a3b008)

~~~json
{
  "source": "00a3b008",
  "target": "0032ff5c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032ff39",
  "offset": 35,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e304c0c1d109e029d04054806054908054a0a054b0c780c1f304c0e00dedd",
  "capture_start": "0032ff39",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00a3b02c`](#insn-00a3b02c)

~~~json
{
  "source": "00a3b02c",
  "target": "009ea92c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b034`](#insn-00a3b034)

~~~json
{
  "source": "00a3b034",
  "target": "00883cc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b03c`](#insn-00a3b03c)

~~~json
{
  "source": "00a3b03c",
  "target": "009e97fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b044`](#insn-00a3b044)

~~~json
{
  "source": "00a3b044",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b048`](#insn-00a3b048)

~~~json
{
  "source": "00a3b048",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b04c`](#insn-00a3b04c)

~~~json
{
  "source": "00a3b04c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b050`](#insn-00a3b050)

~~~json
{
  "source": "00a3b050",
  "target": "009e97e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b058`](#insn-00a3b058)

~~~json
{
  "source": "00a3b058",
  "target": "009e97e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b060`](#insn-00a3b060)

~~~json
{
  "source": "00a3b060",
  "target": "00a3b098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b068`](#insn-00a3b068)

~~~json
{
  "source": "00a3b068",
  "target": "00a3b07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b06c`](#insn-00a3b06c)

~~~json
{
  "source": "00a3b06c",
  "target": "00a3b0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b070`](#insn-00a3b070)

~~~json
{
  "source": "00a3b070",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b078`](#insn-00a3b078)

~~~json
{
  "source": "00a3b078",
  "target": "00a3b084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b07c`](#insn-00a3b07c)

~~~json
{
  "source": "00a3b07c",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b088`](#insn-00a3b088)

~~~json
{
  "source": "00a3b088",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b08c`](#insn-00a3b08c)

~~~json
{
  "source": "00a3b08c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b090`](#insn-00a3b090)

~~~json
{
  "source": "00a3b090",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b094`](#insn-00a3b094)

~~~json
{
  "source": "00a3b094",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b0ac`](#insn-00a3b0ac)

~~~json
{
  "source": "00a3b0ac",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b0b0`](#insn-00a3b0b0)

~~~json
{
  "source": "00a3b0b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b0b4`](#insn-00a3b0b4)

~~~json
{
  "source": "00a3b0b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b0b8`](#insn-00a3b0b8)

~~~json
{
  "source": "00a3b0b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b0bc`](#insn-00a3b0bc)

~~~json
{
  "source": "00a3b0bc",
  "target": "0041c8f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3b0c0`](#insn-00a3b0c0)

~~~json
{
  "source": "00a3b0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b0c4`](#insn-00a3b0c4)

~~~json
{
  "source": "00a3b0c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3b0c8`](#insn-00a3b0c8)

~~~json
{
  "source": "00a3b0c8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
