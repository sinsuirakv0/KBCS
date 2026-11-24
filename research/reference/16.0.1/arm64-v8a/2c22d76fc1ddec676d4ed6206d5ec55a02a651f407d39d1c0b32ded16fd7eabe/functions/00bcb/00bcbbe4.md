# 00bcbbe4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcb7bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-3719f746ef50098c9a885ae6e278e0b6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbc80`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-87446524a28dabb3f453386db89b4c78)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbbe4",
  "name": "_ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0022511a7c4b5e5f7bab9569182856fa624ee9e1ca8b3422a0c9711f6eb1da5d",
  "source_text_sha256": "0022511a7c4b5e5f7bab9569182856fa624ee9e1ca8b3422a0c9711f6eb1da5d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbbe4",
        "00bcbc4b"
      ]
    ],
    "bytes_sha256": "cfc0922b1b646457e0352516ad896d5b1f1e8508291c8067bc37c513f441e31d",
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

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ad50](../00c5a/00c5ad50.md)
- [00c5ae10](../00c5a/00c5ae10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 574 bytes

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
                    /* catch() { ... } // from try @ 00bcbbc8 with catch @ 00bcbc2c */
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x100);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbbe4"></a> `00bcbbe4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbbe8"></a> `00bcbbe8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbec"></a> `00bcbbec` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbf0"></a> `00bcbbf0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcbbf4"></a> `00bcbbf4` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00bcbbf8"></a> `00bcbbf8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcbbfc"></a> `00bcbbfc` | `b4 62 00 91` | add x20,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bcbc00"></a> `00bcbc00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbc04"></a> `00bcbc04` | `7f 3b 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc08"></a> `00bcbc08` | `b5 32 40 f9` | ldr x21,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bcbc0c"></a> `00bcbc0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbc10"></a> `00bcbc10` | `80 3b 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc14"></a> `00bcbc14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbc18"></a> `00bcbc18` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcbc1c"></a> `00bcbc1c` | `15 3c 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc20"></a> `00bcbc20` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcbc24"></a> `00bcbc24` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbc28"></a> `00bcbc28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbc2c"></a> `00bcbc2c` | `79 3c 02 94` | bl 0x00c5ae10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc30"></a> `00bcbc30` | `a1 02 04 91` | add x1,x21,#0x100 | `FALL_THROUGH`
<a id="insn-00bcbc34"></a> `00bcbc34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbc38"></a> `00bcbc38` | `46 3c 02 94` | bl 0x00c5ad50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc3c"></a> `00bcbc3c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbc40"></a> `00bcbc40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc44"></a> `00bcbc44` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbc48"></a> `00bcbc48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbbe4`](#insn-00bcbbe4) 範囲 `[['00bcbbe4', '00bcbc2b']]`
  - `FALL_THROUGH` [`00bcbc28`](#insn-00bcbc28) → [`00bcbc2c`](#insn-00bcbc2c)
- ブロック [`00bcbc2c`](#insn-00bcbc2c) 範囲 `[['00bcbc2c', '00bcbc4b']]`

## 命令位置別の参照

- [`00bcbbe4`](#insn-00bcbbe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbe8`](#insn-00bcbbe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbec`](#insn-00bcbbec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc04`](#insn-00bcbc04) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc10`](#insn-00bcbc10) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc1c`](#insn-00bcbc1c) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc2c`](#insn-00bcbc2c) → [`00c5ae10`](../00c5a/00c5ae10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae10` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc38`](#insn-00bcbc38) → [`00c5ad50`](../00c5a/00c5ad50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad50` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc3c`](#insn-00bcbc3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc40`](#insn-00bcbc40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbbe4`](#insn-00bcbbe4)

~~~json
{
  "source": "00bcbbe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbe8`](#insn-00bcbbe8)

~~~json
{
  "source": "00bcbbe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbec`](#insn-00bcbbec)

~~~json
{
  "source": "00bcbbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc04`](#insn-00bcbc04)

~~~json
{
  "source": "00bcbc04",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc10`](#insn-00bcbc10)

~~~json
{
  "source": "00bcbc10",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc1c`](#insn-00bcbc1c)

~~~json
{
  "source": "00bcbc1c",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc2c`](#insn-00bcbc2c)

~~~json
{
  "source": "00bcbc2c",
  "target": "00c5ae10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc38`](#insn-00bcbc38)

~~~json
{
  "source": "00bcbc38",
  "target": "00c5ad50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc3c`](#insn-00bcbc3c)

~~~json
{
  "source": "00bcbc3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc40`](#insn-00bcbc40)

~~~json
{
  "source": "00bcbc40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
