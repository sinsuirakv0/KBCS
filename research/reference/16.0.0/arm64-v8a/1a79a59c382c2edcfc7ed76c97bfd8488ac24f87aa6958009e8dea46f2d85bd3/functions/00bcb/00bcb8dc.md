# 00bcb8dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c3dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c3dc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-21354840314cb3786b186174d6e17dd5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbd04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-b1f20159e908f7978682549727d1201d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb8dc",
  "name": "_ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e6d2ea5220132a2cedce5269925a411c3dc91ebc80d9f36729446f359cf74c43",
  "source_text_sha256": "e6d2ea5220132a2cedce5269925a411c3dc91ebc80d9f36729446f359cf74c43",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb8dc",
        "00bcb943"
      ]
    ],
    "bytes_sha256": "256b89d9d3f820b1a4dd8a390edac5c6d3d6273195f433fbade97299322e7cb6",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5a950](../00c5a/00c5a950.md)
- [00c5aa10](../00c5a/00c5aa10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 500 bytes

~~~c

void _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv(long param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  
  lVar2 = *param_2;
  lVar1 = lVar2 + 0x18;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar2 = *(long *)(lVar2 + 0x60);
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = 0;
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x1c0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb8dc"></a> `00bcb8dc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcb8e0"></a> `00bcb8e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb8e4"></a> `00bcb8e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb8e8"></a> `00bcb8e8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcb8ec"></a> `00bcb8ec` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00bcb8f0"></a> `00bcb8f0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcb8f4"></a> `00bcb8f4` | `b4 62 00 91` | add x20,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bcb8f8"></a> `00bcb8f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb8fc"></a> `00bcb8fc` | `41 3b 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb900"></a> `00bcb900` | `b5 32 40 f9` | ldr x21,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bcb904"></a> `00bcb904` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb908"></a> `00bcb908` | `42 3b 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb90c"></a> `00bcb90c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb910"></a> `00bcb910` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcb914"></a> `00bcb914` | `d7 3b 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb918"></a> `00bcb918` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcb91c"></a> `00bcb91c` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcb920"></a> `00bcb920` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb924"></a> `00bcb924` | `3b 3c 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb928"></a> `00bcb928` | `a1 02 07 91` | add x1,x21,#0x1c0 | `FALL_THROUGH`
<a id="insn-00bcb92c"></a> `00bcb92c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb930"></a> `00bcb930` | `08 3c 02 94` | bl 0x00c5a950 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb934"></a> `00bcb934` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb938"></a> `00bcb938` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb93c"></a> `00bcb93c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcb940"></a> `00bcb940` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb8dc`](#insn-00bcb8dc) 範囲 `[['00bcb8dc', '00bcb943']]`

## 命令位置別の参照

- [`00bcb8dc`](#insn-00bcb8dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb8e0`](#insn-00bcb8e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb8e4`](#insn-00bcb8e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb8fc`](#insn-00bcb8fc) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcb908`](#insn-00bcb908) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcb914`](#insn-00bcb914) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bcb924`](#insn-00bcb924) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcb930`](#insn-00bcb930) → [`00c5a950`](../00c5a/00c5a950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a950` · 推定シンボル `None` · 推定型 `None`
- [`00bcb934`](#insn-00bcb934) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb938`](#insn-00bcb938) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb8dc`](#insn-00bcb8dc)

~~~json
{
  "source": "00bcb8dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb8e0`](#insn-00bcb8e0)

~~~json
{
  "source": "00bcb8e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb8e4`](#insn-00bcb8e4)

~~~json
{
  "source": "00bcb8e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb8fc`](#insn-00bcb8fc)

~~~json
{
  "source": "00bcb8fc",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb908`](#insn-00bcb908)

~~~json
{
  "source": "00bcb908",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb914`](#insn-00bcb914)

~~~json
{
  "source": "00bcb914",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb924`](#insn-00bcb924)

~~~json
{
  "source": "00bcb924",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb930`](#insn-00bcb930)

~~~json
{
  "source": "00bcb930",
  "target": "00c5a950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb934`](#insn-00bcb934)

~~~json
{
  "source": "00bcb934",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb938`](#insn-00bcb938)

~~~json
{
  "source": "00bcb938",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
