# 00bdc5fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdc1d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-dcb19dcd85359e1b5b817709b5af940a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdc698`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc698.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-f88f6c6cd42d16f76ce390092d4b2bb5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdc5fc",
  "name": "_ZN8firebase4auth10AuthResultC2ERKS1_",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c84ead858a85688626a5dca834c5dbd377a1758b8a81b627f3eda33861fb56a6",
  "source_text_sha256": "c84ead858a85688626a5dca834c5dbd377a1758b8a81b627f3eda33861fb56a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdc5fc",
        "00bdc657"
      ]
    ],
    "bytes_sha256": "f469cd1f24c8c7264fe1d2662ed7a301e09195ca8950c05151fccc4c8511860a",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ddf0](../00c5d/00c5ddf0.md)

## 呼び出し先

- [00c5aa40](../00c5a/00c5aa40.md)
- [00c5dd60](../00c5d/00c5dd60.md)
- [00c5de20](../00c5d/00c5de20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 680 bytes

~~~c

void _ZN8firebase4auth10AuthResultC2ERKS1_(long param_1,long param_2)

{
  _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_();
  *(undefined8 *)(param_1 + 0x70) = 0;
  *(undefined4 *)(param_1 + 0x78) = 0;
  *(undefined8 *)(param_1 + 0x80) = 0;
  *(undefined8 *)(param_1 + 0x88) = 0;
  *(undefined8 *)(param_1 + 0x90) = 0;
  _ZN8firebase4auth10CredentialaSERKS1_((undefined8 *)(param_1 + 0x70),param_2 + 0x70);
                    /* try { // try from 00bdc640 to 00cdc64b has its CatchHandler @ 00bdee78 */
  _ZN8firebase4auth4UserC1ERKS1_(param_1 + 0x98,param_2 + 0x98);
                    /* try { // try from 00bdc650 to 00cdc68f has its CatchHandler @ 00bdeecc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdc5fc"></a> `00bdc5fc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdc600"></a> `00bdc600` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc604"></a> `00bdc604` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc608"></a> `00bdc608` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdc60c"></a> `00bdc60c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bdc610"></a> `00bdc610` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdc614"></a> `00bdc614` | `03 06 02 94` | bl 0x00c5de20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc618"></a> `00bdc618` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bdc61c"></a> `00bdc61c` | `9f 0e 07 f8` | str xzr,[x20, #0x70]! | `FALL_THROUGH`
<a id="insn-00bdc620"></a> `00bdc620` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00bdc624"></a> `00bdc624` | `a1 c2 01 91` | add x1,x21,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc628"></a> `00bdc628` | `9f 0a 00 b9` | str wzr,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bdc62c"></a> `00bdc62c` | `df 0e 01 f8` | str xzr,[x22, #0x10]! | `FALL_THROUGH`
<a id="insn-00bdc630"></a> `00bdc630` | `9f fe 01 a9` | stp xzr,xzr,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bdc634"></a> `00bdc634` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdc638"></a> `00bdc638` | `ca 05 02 94` | bl 0x00c5dd60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc63c"></a> `00bdc63c` | `60 62 02 91` | add x0,x19,#0x98 | `FALL_THROUGH`
<a id="insn-00bdc640"></a> `00bdc640` | `a1 62 02 91` | add x1,x21,#0x98 | `FALL_THROUGH`
<a id="insn-00bdc644"></a> `00bdc644` | `ff f8 01 94` | bl 0x00c5aa40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc648"></a> `00bdc648` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc64c"></a> `00bdc64c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc650"></a> `00bdc650` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdc654"></a> `00bdc654` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdc5fc`](#insn-00bdc5fc) 範囲 `[['00bdc5fc', '00bdc63f']]`
  - `FALL_THROUGH` [`00bdc63c`](#insn-00bdc63c) → [`00bdc640`](#insn-00bdc640)
- ブロック [`00bdc640`](#insn-00bdc640) 範囲 `[['00bdc640', '00bdc64f']]`
  - `FALL_THROUGH` [`00bdc64c`](#insn-00bdc64c) → [`00bdc650`](#insn-00bdc650)
- ブロック [`00bdc650`](#insn-00bdc650) 範囲 `[['00bdc650', '00bdc657']]`

## 命令位置別の参照

- [`00bdc5fc`](#insn-00bdc5fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc600`](#insn-00bdc600) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc604`](#insn-00bdc604) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc614`](#insn-00bdc614) → [`00c5de20`](../00c5d/00c5de20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de20` · 推定シンボル `None` · 推定型 `None`
- [`00bdc638`](#insn-00bdc638) → [`00c5dd60`](../00c5d/00c5dd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd60` · 推定シンボル `None` · 推定型 `None`
- [`00bdc644`](#insn-00bdc644) → [`00c5aa40`](../00c5a/00c5aa40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa40` · 推定シンボル `None` · 推定型 `None`
- [`00bdc648`](#insn-00bdc648) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc64c`](#insn-00bdc64c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdc5fc`](#insn-00bdc5fc)

~~~json
{
  "source": "00bdc5fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc600`](#insn-00bdc600)

~~~json
{
  "source": "00bdc600",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc604`](#insn-00bdc604)

~~~json
{
  "source": "00bdc604",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc614`](#insn-00bdc614)

~~~json
{
  "source": "00bdc614",
  "target": "00c5de20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc638`](#insn-00bdc638)

~~~json
{
  "source": "00bdc638",
  "target": "00c5dd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc644`](#insn-00bdc644)

~~~json
{
  "source": "00bdc644",
  "target": "00c5aa40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc648`](#insn-00bdc648)

~~~json
{
  "source": "00bdc648",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc64c`](#insn-00bdc64c)

~~~json
{
  "source": "00bdc64c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
