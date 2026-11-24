# 00bcb7bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c2bc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c2bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-0212e5b07085ab205b31b03aa6211080)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbbe4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-3719f746ef50098c9a885ae6e278e0b6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb7bc",
  "name": "_ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "629c335216e227598cd1c1a8fb6b2e2ab3f48f4c25505a8f4814be4fa3587722",
  "source_text_sha256": "629c335216e227598cd1c1a8fb6b2e2ab3f48f4c25505a8f4814be4fa3587722",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb7bc",
        "00bcb823"
      ]
    ],
    "bytes_sha256": "23e752341d1928f2cabd1ae273aceee9f2136314fbaba76c92eb7ca72d767463",
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

## 疑似コード / UTF-8 487 bytes

~~~c

void _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv(long param_1,long *param_2)

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
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x100);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb7bc"></a> `00bcb7bc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcb7c0"></a> `00bcb7c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb7c4"></a> `00bcb7c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb7c8"></a> `00bcb7c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcb7cc"></a> `00bcb7cc` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00bcb7d0"></a> `00bcb7d0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcb7d4"></a> `00bcb7d4` | `b4 62 00 91` | add x20,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bcb7d8"></a> `00bcb7d8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb7dc"></a> `00bcb7dc` | `89 3b 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb7e0"></a> `00bcb7e0` | `b5 32 40 f9` | ldr x21,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bcb7e4"></a> `00bcb7e4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb7e8"></a> `00bcb7e8` | `8a 3b 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb7ec"></a> `00bcb7ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb7f0"></a> `00bcb7f0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcb7f4"></a> `00bcb7f4` | `1f 3c 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb7f8"></a> `00bcb7f8` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcb7fc"></a> `00bcb7fc` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcb800"></a> `00bcb800` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb804"></a> `00bcb804` | `83 3c 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb808"></a> `00bcb808` | `a1 02 04 91` | add x1,x21,#0x100 | `FALL_THROUGH`
<a id="insn-00bcb80c"></a> `00bcb80c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb810"></a> `00bcb810` | `50 3c 02 94` | bl 0x00c5a950 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb814"></a> `00bcb814` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb818"></a> `00bcb818` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb81c"></a> `00bcb81c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcb820"></a> `00bcb820` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb7bc`](#insn-00bcb7bc) 範囲 `[['00bcb7bc', '00bcb823']]`

## 命令位置別の参照

- [`00bcb7bc`](#insn-00bcb7bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb7c0`](#insn-00bcb7c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb7c4`](#insn-00bcb7c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb7dc`](#insn-00bcb7dc) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcb7e8`](#insn-00bcb7e8) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcb7f4`](#insn-00bcb7f4) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bcb804`](#insn-00bcb804) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcb810`](#insn-00bcb810) → [`00c5a950`](../00c5a/00c5a950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a950` · 推定シンボル `None` · 推定型 `None`
- [`00bcb814`](#insn-00bcb814) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb818`](#insn-00bcb818) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb7bc`](#insn-00bcb7bc)

~~~json
{
  "source": "00bcb7bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb7c0`](#insn-00bcb7c0)

~~~json
{
  "source": "00bcb7c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb7c4`](#insn-00bcb7c4)

~~~json
{
  "source": "00bcb7c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb7dc`](#insn-00bcb7dc)

~~~json
{
  "source": "00bcb7dc",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb7e8`](#insn-00bcb7e8)

~~~json
{
  "source": "00bcb7e8",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb7f4`](#insn-00bcb7f4)

~~~json
{
  "source": "00bcb7f4",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb804`](#insn-00bcb804)

~~~json
{
  "source": "00bcb804",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb810`](#insn-00bcb810)

~~~json
{
  "source": "00bcb810",
  "target": "00c5a950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb814`](#insn-00bcb814)

~~~json
{
  "source": "00bcb814",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb818`](#insn-00bcb818)

~~~json
{
  "source": "00bcb818",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
