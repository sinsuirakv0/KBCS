# 00bfbb7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb754`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb754.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-213349b644ce41e0accc3efc6e37f73a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbc18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-9ce5ba7bcc2dfcfda4eb330c09352acd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbb7c",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efd482e09240dcf09da7687dffb4afb9ee63a852910ba2bbb76fec77137ddb6f",
  "source_text_sha256": "efd482e09240dcf09da7687dffb4afb9ee63a852910ba2bbb76fec77137ddb6f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbb7c",
        "00bfbbf7"
      ]
    ],
    "bytes_sha256": "0c2f6937f27507f5851d53d9401bee1bc88e180e9cdca0107018e205a741b37a",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c5e2d0](../00c5e/00c5e2d0.md)
- [00c5e310](../00c5e/00c5e310.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 674 bytes

~~~c

long _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_(long param_1,long param_2)

{
  undefined4 uVar1;
  
  if (param_1 != param_2) {
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,0);
    _ZNSt6__ndk18ios_base7copyfmtERKS0_(param_1,param_2);
    uVar1 = *(undefined4 *)(param_2 + 0x90);
    *(undefined8 *)(param_1 + 0x88) = *(undefined8 *)(param_2 + 0x88);
    *(undefined4 *)(param_1 + 0x90) = uVar1;
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,2);
    *(undefined4 *)(param_1 + 0x24) = *(undefined4 *)(param_2 + 0x24);
    _ZNSt6__ndk18ios_base5clearEj(param_1,*(undefined4 *)(param_1 + 0x20));
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbb7c"></a> `00bfbb7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbb80"></a> `00bfbb80` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbb84"></a> `00bfbb84` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbb88"></a> `00bfbb88` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbb8c"></a> `00bfbb8c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbb90"></a> `00bfbb90` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bfbb94"></a> `00bfbb94` | `80 02 00 54` | b.eq 0x00bfbbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bfbb98"></a> `00bfbb98` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfbb9c"></a> `00bfbb9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbba0"></a> `00bfbba0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bfbba4"></a> `00bfbba4` | `cb 89 01 94` | bl 0x00c5e2d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbba8"></a> `00bfbba8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbbac"></a> `00bfbbac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfbbb0"></a> `00bfbbb0` | `d8 89 01 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbbb4"></a> `00bfbbb4` | `88 46 40 f9` | ldr x8,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bfbbb8"></a> `00bfbbb8` | `89 92 40 b9` | ldr w9,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bfbbbc"></a> `00bfbbbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbbc0"></a> `00bfbbc0` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00bfbbc4"></a> `00bfbbc4` | `68 46 00 f9` | str x8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bfbbc8"></a> `00bfbbc8` | `69 92 00 b9` | str w9,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bfbbcc"></a> `00bfbbcc` | `c1 89 01 94` | bl 0x00c5e2d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbbd0"></a> `00bfbbd0` | `88 26 40 b9` | ldr w8,[x20, #0x24] | `FALL_THROUGH`
<a id="insn-00bfbbd4"></a> `00bfbbd4` | `61 22 40 b9` | ldr w1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbbd8"></a> `00bfbbd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbbdc"></a> `00bfbbdc` | `68 26 00 b9` | str w8,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00bfbbe0"></a> `00bfbbe0` | `b0 71 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbbe4"></a> `00bfbbe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbbe8"></a> `00bfbbe8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbbec"></a> `00bfbbec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbbf0"></a> `00bfbbf0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbbf4"></a> `00bfbbf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbb7c`](#insn-00bfbb7c) 範囲 `[['00bfbb7c', '00bfbb97']]`
  - `CONDITIONAL_JUMP` [`00bfbb94`](#insn-00bfbb94) → [`00bfbbe4`](#insn-00bfbbe4)
  - `FALL_THROUGH` [`00bfbb94`](#insn-00bfbb94) → [`00bfbb98`](#insn-00bfbb98)
- ブロック [`00bfbb98`](#insn-00bfbb98) 範囲 `[['00bfbb98', '00bfbbe3']]`
  - `FALL_THROUGH` [`00bfbbe0`](#insn-00bfbbe0) → [`00bfbbe4`](#insn-00bfbbe4)
- ブロック [`00bfbbe4`](#insn-00bfbbe4) 範囲 `[['00bfbbe4', '00bfbbf7']]`

## 命令位置別の参照

- [`00bfbb80`](#insn-00bfbb80) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb84`](#insn-00bfbb84) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb94`](#insn-00bfbb94) → [`00bfbbe4`](#insn-00bfbbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbba4`](#insn-00bfbba4) → [`00c5e2d0`](../00c5e/00c5e2d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbbb0`](#insn-00bfbbb0) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00bfbbcc`](#insn-00bfbbcc) → [`00c5e2d0`](../00c5e/00c5e2d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbbe0`](#insn-00bfbbe0) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbbe8`](#insn-00bfbbe8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbbec`](#insn-00bfbbec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbb80`](#insn-00bfbb80)

~~~json
{
  "source": "00bfbb80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbb84`](#insn-00bfbb84)

~~~json
{
  "source": "00bfbb84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbb94`](#insn-00bfbb94)

~~~json
{
  "source": "00bfbb94",
  "target": "00bfbbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbba4`](#insn-00bfbba4)

~~~json
{
  "source": "00bfbba4",
  "target": "00c5e2d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbbb0`](#insn-00bfbbb0)

~~~json
{
  "source": "00bfbbb0",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbbcc`](#insn-00bfbbcc)

~~~json
{
  "source": "00bfbbcc",
  "target": "00c5e2d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbbe0`](#insn-00bfbbe0)

~~~json
{
  "source": "00bfbbe0",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbbe8`](#insn-00bfbbe8)

~~~json
{
  "source": "00bfbbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbbec`](#insn-00bfbbec)

~~~json
{
  "source": "00bfbbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
