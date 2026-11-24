# 00bfca1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfba28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfba28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-0d4204ed8efc93c8f13130a82d68aebd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfca1c",
  "name": "_ZNSt6__ndk18ios_base4swapERS0_",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a46d2dd185159a3a076b8f579a6b9ffac1cf7de6ece5ee974fae821654f89d8",
  "source_text_sha256": "7a46d2dd185159a3a076b8f579a6b9ffac1cf7de6ece5ee974fae821654f89d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfca1c",
        "00bfcb37"
      ]
    ],
    "bytes_sha256": "37c6dde55203c6b7a3c8a93a5cf50320900c6ba915441dccc23fbbcc7f47cbd8",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5f3c0](../00c5f/00c5f3c0.md)

## 呼び出し先

- [00c59330](../00c59/00c59330.md)
- [00c5b870](../00c5b/00c5b870.md)
- [00c5f380](../00c5f/00c5f380.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2828 bytes

~~~c

void _ZNSt6__ndk18ios_base4swapERS0_(long param_1,long param_2)

{
  undefined8 uVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined1 auStack_28 [8];
  
  uVar5 = *(undefined8 *)(param_2 + 0x10);
  uVar2 = *(undefined4 *)(param_1 + 8);
  *(undefined4 *)(param_1 + 8) = *(undefined4 *)(param_2 + 8);
  uVar4 = *(undefined8 *)(param_1 + 0x10);
  *(undefined8 *)(param_1 + 0x10) = uVar5;
  *(undefined4 *)(param_2 + 8) = uVar2;
  *(undefined8 *)(param_2 + 0x10) = uVar4;
  uVar2 = *(undefined4 *)(param_2 + 0x20);
  uVar4 = *(undefined8 *)(param_1 + 0x18);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  uVar3 = *(undefined4 *)(param_1 + 0x20);
  *(undefined4 *)(param_1 + 0x20) = uVar2;
  *(undefined4 *)(param_2 + 0x20) = uVar3;
  uVar2 = *(undefined4 *)(param_1 + 0x24);
  *(undefined8 *)(param_2 + 0x18) = uVar4;
  *(undefined4 *)(param_1 + 0x24) = *(undefined4 *)(param_2 + 0x24);
  *(undefined4 *)(param_2 + 0x24) = uVar2;
  _ZNSt6__ndk16localeC1ERKS0_(auStack_28,param_1 + 0x30);
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 0x30,param_2 + 0x30);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 0x30,auStack_28);
  _ZNSt6__ndk16localeD1Ev(auStack_28);
  uVar4 = *(undefined8 *)(param_1 + 0x38);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_2 + 0x38) = uVar4;
  uVar5 = *(undefined8 *)(param_2 + 0x48);
  uVar4 = *(undefined8 *)(param_1 + 0x40);
  uVar1 = *(undefined8 *)(param_1 + 0x48);
  *(undefined8 *)(param_1 + 0x40) = *(undefined8 *)(param_2 + 0x40);
  *(undefined8 *)(param_1 + 0x48) = uVar5;
  *(undefined8 *)(param_2 + 0x40) = uVar4;
  *(undefined8 *)(param_2 + 0x48) = uVar1;
  uVar5 = *(undefined8 *)(param_2 + 0x58);
  uVar4 = *(undefined8 *)(param_1 + 0x50);
  uVar1 = *(undefined8 *)(param_1 + 0x58);
  *(undefined8 *)(param_1 + 0x50) = *(undefined8 *)(param_2 + 0x50);
  *(undefined8 *)(param_1 + 0x58) = uVar5;
  *(undefined8 *)(param_2 + 0x50) = uVar4;
  uVar4 = *(undefined8 *)(param_1 + 0x60);
  *(undefined8 *)(param_1 + 0x60) = *(undefined8 *)(param_2 + 0x60);
  *(undefined8 *)(param_2 + 0x58) = uVar1;
  *(undefined8 *)(param_2 + 0x60) = uVar4;
  uVar5 = *(undefined8 *)(param_2 + 0x70);
  uVar4 = *(undefined8 *)(param_1 + 0x68);
  uVar1 = *(undefined8 *)(param_1 + 0x70);
  *(undefined8 *)(param_1 + 0x68) = *(undefined8 *)(param_2 + 0x68);
  *(undefined8 *)(param_1 + 0x70) = uVar5;
  *(undefined8 *)(param_2 + 0x68) = uVar4;
  uVar4 = *(undefined8 *)(param_1 + 0x78);
  *(undefined8 *)(param_1 + 0x78) = *(undefined8 *)(param_2 + 0x78);
  *(undefined8 *)(param_2 + 0x70) = uVar1;
  *(undefined8 *)(param_2 + 0x78) = uVar4;
  uVar4 = *(undefined8 *)(param_1 + 0x80);
  *(undefined8 *)(param_1 + 0x80) = *(undefined8 *)(param_2 + 0x80);
  *(undefined8 *)(param_2 + 0x80) = uVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfca1c"></a> `00bfca1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfca20"></a> `00bfca20` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfca24"></a> `00bfca24` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfca28"></a> `00bfca28` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfca2c"></a> `00bfca2c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfca30"></a> `00bfca30` | `28 08 40 b9` | ldr w8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bfca34"></a> `00bfca34` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bfca38"></a> `00bfca38` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfca3c"></a> `00bfca3c` | `0a 08 40 b9` | ldr w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfca40"></a> `00bfca40` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfca44"></a> `00bfca44` | `08 08 00 b9` | str w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfca48"></a> `00bfca48` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfca4c"></a> `00bfca4c` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfca50"></a> `00bfca50` | `29 0c 40 f9` | ldr x9,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bfca54"></a> `00bfca54` | `2a 08 00 b9` | str w10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bfca58"></a> `00bfca58` | `28 08 00 f9` | str x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bfca5c"></a> `00bfca5c` | `28 20 40 b9` | ldr w8,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bfca60"></a> `00bfca60` | `0a 0c 40 f9` | ldr x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfca64"></a> `00bfca64` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfca68"></a> `00bfca68` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfca6c"></a> `00bfca6c` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfca70"></a> `00bfca70` | `29 20 00 b9` | str w9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bfca74"></a> `00bfca74` | `28 24 40 b9` | ldr w8,[x1, #0x24] | `FALL_THROUGH`
<a id="insn-00bfca78"></a> `00bfca78` | `09 24 40 b9` | ldr w9,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00bfca7c"></a> `00bfca7c` | `2a 0c 00 f9` | str x10,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bfca80"></a> `00bfca80` | `08 24 00 b9` | str w8,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00bfca84"></a> `00bfca84` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfca88"></a> `00bfca88` | `29 24 00 b9` | str w9,[x1, #0x24] | `FALL_THROUGH`
<a id="insn-00bfca8c"></a> `00bfca8c` | `81 c2 00 91` | add x1,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bfca90"></a> `00bfca90` | `78 7b 01 94` | bl 0x00c5b870 | `UNCONDITIONAL_CALL`
<a id="insn-00bfca94"></a> `00bfca94` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bfca98"></a> `00bfca98` | `61 c2 00 91` | add x1,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bfca9c"></a> `00bfca9c` | `39 8a 01 94` | bl 0x00c5f380 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcaa0"></a> `00bfcaa0` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcaa4"></a> `00bfcaa4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcaa8"></a> `00bfcaa8` | `36 8a 01 94` | bl 0x00c5f380 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcaac"></a> `00bfcaac` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcab0"></a> `00bfcab0` | `20 72 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcab4"></a> `00bfcab4` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bfcab8"></a> `00bfcab8` | `89 1e 40 f9` | ldr x9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bfcabc"></a> `00bfcabc` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bfcac0"></a> `00bfcac0` | `69 1e 00 f9` | str x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bfcac4"></a> `00bfcac4` | `68 26 44 a9` | ldp x8,x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bfcac8"></a> `00bfcac8` | `8a 2e 44 a9` | ldp x10,x11,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bfcacc"></a> `00bfcacc` | `88 26 04 a9` | stp x8,x9,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bfcad0"></a> `00bfcad0` | `6a 2e 04 a9` | stp x10,x11,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bfcad4"></a> `00bfcad4` | `68 26 45 a9` | ldp x8,x9,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00bfcad8"></a> `00bfcad8` | `8a 2e 45 a9` | ldp x10,x11,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bfcadc"></a> `00bfcadc` | `88 26 05 a9` | stp x8,x9,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bfcae0"></a> `00bfcae0` | `6a 2a 00 f9` | str x10,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00bfcae4"></a> `00bfcae4` | `68 32 40 f9` | ldr x8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bfcae8"></a> `00bfcae8` | `89 32 40 f9` | ldr x9,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-00bfcaec"></a> `00bfcaec` | `88 32 00 f9` | str x8,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-00bfcaf0"></a> `00bfcaf0` | `6b a6 05 a9` | stp x11,x9,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfcaf4"></a> `00bfcaf4` | `68 a6 46 a9` | ldp x8,x9,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bfcaf8"></a> `00bfcaf8` | `8a ae 46 a9` | ldp x10,x11,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00bfcafc"></a> `00bfcafc` | `88 a6 06 a9` | stp x8,x9,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00bfcb00"></a> `00bfcb00` | `6a 36 00 f9` | str x10,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bfcb04"></a> `00bfcb04` | `68 3e 40 f9` | ldr x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bfcb08"></a> `00bfcb08` | `89 3e 40 f9` | ldr x9,[x20, #0x78] | `FALL_THROUGH`
<a id="insn-00bfcb0c"></a> `00bfcb0c` | `88 3e 00 f9` | str x8,[x20, #0x78] | `FALL_THROUGH`
<a id="insn-00bfcb10"></a> `00bfcb10` | `6b 26 07 a9` | stp x11,x9,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfcb14"></a> `00bfcb14` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bfcb18"></a> `00bfcb18` | `89 42 40 f9` | ldr x9,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00bfcb1c"></a> `00bfcb1c` | `88 42 00 f9` | str x8,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00bfcb20"></a> `00bfcb20` | `69 42 00 f9` | str x9,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bfcb24"></a> `00bfcb24` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcb28"></a> `00bfcb28` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcb2c"></a> `00bfcb2c` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcb30"></a> `00bfcb30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcb34"></a> `00bfcb34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfca1c`](#insn-00bfca1c) 範囲 `[['00bfca1c', '00bfcb37']]`

## 命令位置別の参照

- [`00bfca24`](#insn-00bfca24) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfca28`](#insn-00bfca28) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfca90`](#insn-00bfca90) → [`00c5b870`](../00c5b/00c5b870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b870` · 推定シンボル `None` · 推定型 `None`
- [`00bfca9c`](#insn-00bfca9c) → [`00c5f380`](../00c5f/00c5f380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f380` · 推定シンボル `None` · 推定型 `None`
- [`00bfcaa8`](#insn-00bfcaa8) → [`00c5f380`](../00c5f/00c5f380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f380` · 推定シンボル `None` · 推定型 `None`
- [`00bfcab0`](#insn-00bfcab0) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb24`](#insn-00bfcb24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb28`](#insn-00bfcb28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfca24`](#insn-00bfca24)

~~~json
{
  "source": "00bfca24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfca28`](#insn-00bfca28)

~~~json
{
  "source": "00bfca28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfca90`](#insn-00bfca90)

~~~json
{
  "source": "00bfca90",
  "target": "00c5b870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfca9c`](#insn-00bfca9c)

~~~json
{
  "source": "00bfca9c",
  "target": "00c5f380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcaa8`](#insn-00bfcaa8)

~~~json
{
  "source": "00bfcaa8",
  "target": "00c5f380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcab0`](#insn-00bfcab0)

~~~json
{
  "source": "00bfcab0",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcb24`](#insn-00bfcb24)

~~~json
{
  "source": "00bfcb24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb28`](#insn-00bfcb28)

~~~json
{
  "source": "00bfcb28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
