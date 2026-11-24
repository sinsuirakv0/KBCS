# 00bffdf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff9cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-a222c3d59edb2456e72ade505c23cb4b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bffe90`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe90.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-b71dc83af5cf6a1159a2afa9a296b233)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffdf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9c62fb3932e93eed1441149527fdad124489992bb30cc6927657248217a277c",
  "source_text_sha256": "d9c62fb3932e93eed1441149527fdad124489992bb30cc6927657248217a277c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffdf4",
        "00bffeaf"
      ]
    ],
    "bytes_sha256": "2304efff07ca62044da3640d9c6378638828ee53dad5c9b5562cdc3fac8b3eab",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58290](../00c58/00c58290.md)
- [00c5a7d0](../00c5a/00c5a7d0.md)
- [00c5e2e0](../00c5e/00c5e2e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1299 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_(long param_1,long param_2)

{
  undefined8 uVar1;
  undefined1 auStack_28 [8];
  
  _ZNSt6__ndk16localeC1ERKS0_(auStack_28,param_1 + 8);
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 8,param_2 + 8);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 8,auStack_28);
  _ZNSt6__ndk16localeD1Ev(auStack_28);
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *(undefined8 *)(param_1 + 0x10) = *(undefined8 *)(param_2 + 0x10);
  *(undefined8 *)(param_2 + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x18);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  *(undefined8 *)(param_2 + 0x18) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x20);
  *(undefined8 *)(param_1 + 0x20) = *(undefined8 *)(param_2 + 0x20);
  *(undefined8 *)(param_2 + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x28);
  *(undefined8 *)(param_1 + 0x28) = *(undefined8 *)(param_2 + 0x28);
  *(undefined8 *)(param_2 + 0x28) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x30) = *(undefined8 *)(param_2 + 0x30);
  *(undefined8 *)(param_2 + 0x30) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x38);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_2 + 0x38) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffdf4"></a> `00bffdf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffdf8"></a> `00bffdf8` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bffdfc"></a> `00bffdfc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffe00"></a> `00bffe00` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe04"></a> `00bffe04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bffe08"></a> `00bffe08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bffe0c"></a> `00bffe0c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bffe10"></a> `00bffe10` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe14"></a> `00bffe14` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe18"></a> `00bffe18` | `6e 6a 01 94` | bl 0x00c5a7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffe1c"></a> `00bffe1c` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe20"></a> `00bffe20` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe24"></a> `00bffe24` | `2f 79 01 94` | bl 0x00c5e2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffe28"></a> `00bffe28` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe2c"></a> `00bffe2c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe30"></a> `00bffe30` | `2c 79 01 94` | bl 0x00c5e2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffe34"></a> `00bffe34` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe38"></a> `00bffe38` | `16 61 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bffe3c"></a> `00bffe3c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bffe40"></a> `00bffe40` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bffe44"></a> `00bffe44` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bffe48"></a> `00bffe48` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bffe4c"></a> `00bffe4c` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bffe50"></a> `00bffe50` | `89 0e 40 f9` | ldr x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bffe54"></a> `00bffe54` | `88 0e 00 f9` | str x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bffe58"></a> `00bffe58` | `69 0e 00 f9` | str x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bffe5c"></a> `00bffe5c` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe60"></a> `00bffe60` | `89 12 40 f9` | ldr x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe64"></a> `00bffe64` | `88 12 00 f9` | str x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe68"></a> `00bffe68` | `69 12 00 f9` | str x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe6c"></a> `00bffe6c` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bffe70"></a> `00bffe70` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bffe74"></a> `00bffe74` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bffe78"></a> `00bffe78` | `69 16 00 f9` | str x9,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bffe7c"></a> `00bffe7c` | `68 1a 40 f9` | ldr x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bffe80"></a> `00bffe80` | `89 1a 40 f9` | ldr x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bffe84"></a> `00bffe84` | `88 1a 00 f9` | str x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bffe88"></a> `00bffe88` | `69 1a 00 f9` | str x9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bffe8c"></a> `00bffe8c` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bffe90"></a> `00bffe90` | `89 1e 40 f9` | ldr x9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bffe94"></a> `00bffe94` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bffe98"></a> `00bffe98` | `69 1e 00 f9` | str x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bffe9c"></a> `00bffe9c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffea0"></a> `00bffea0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffea4"></a> `00bffea4` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bffea8"></a> `00bffea8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffeac"></a> `00bffeac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffdf4`](#insn-00bffdf4) 範囲 `[['00bffdf4', '00bffeaf']]`

## 命令位置別の参照

- [`00bffdfc`](#insn-00bffdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffe00`](#insn-00bffe00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffe18`](#insn-00bffe18) → [`00c5a7d0`](../00c5a/00c5a7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7d0` · 推定シンボル `None` · 推定型 `None`
- [`00bffe24`](#insn-00bffe24) → [`00c5e2e0`](../00c5e/00c5e2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2e0` · 推定シンボル `None` · 推定型 `None`
- [`00bffe30`](#insn-00bffe30) → [`00c5e2e0`](../00c5e/00c5e2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2e0` · 推定シンボル `None` · 推定型 `None`
- [`00bffe38`](#insn-00bffe38) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bffe9c`](#insn-00bffe9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffea0`](#insn-00bffea0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffdfc`](#insn-00bffdfc)

~~~json
{
  "source": "00bffdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffe00`](#insn-00bffe00)

~~~json
{
  "source": "00bffe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffe18`](#insn-00bffe18)

~~~json
{
  "source": "00bffe18",
  "target": "00c5a7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe24`](#insn-00bffe24)

~~~json
{
  "source": "00bffe24",
  "target": "00c5e2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe30`](#insn-00bffe30)

~~~json
{
  "source": "00bffe30",
  "target": "00c5e2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe38`](#insn-00bffe38)

~~~json
{
  "source": "00bffe38",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe9c`](#insn-00bffe9c)

~~~json
{
  "source": "00bffe9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffea0`](#insn-00bffea0)

~~~json
{
  "source": "00bffea0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
