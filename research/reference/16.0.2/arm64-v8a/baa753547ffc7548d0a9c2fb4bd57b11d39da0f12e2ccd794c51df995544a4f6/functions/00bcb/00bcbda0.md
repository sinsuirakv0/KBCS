# 00bcbda0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbd04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-48a8d505f2c820075fc409fe3481a2be)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bccd94`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccd94.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-e49c0cf600ab758503269cee547962e5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbda0",
  "name": "_ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b92ca009d91e748a455f385db0328fadfd5cbb4e6b108fd952576a5330f5701",
  "source_text_sha256": "5b92ca009d91e748a455f385db0328fadfd5cbb4e6b108fd952576a5330f5701",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbda0",
        "00bcbe07"
      ]
    ],
    "bytes_sha256": "68d44450ed60f527c15d247123110028db46d4eac277d3ff33a4f7139101d8a3",
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

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ae20](../00c5a/00c5ae20.md)
- [00c5aee0](../00c5a/00c5aee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 781 bytes

~~~c

void _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv(long param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  
  lVar2 = *param_2;
  lVar1 = lVar2 + 0x18;
                    /* catch() { ... } // from try @ 00bcbdfc with catch @ 00bcbdbc */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar2 = *(long *)(lVar2 + 0x60);
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = 0;
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bcbdf4 to 00ccbdfb has its CatchHandler @ 00bcbee8 */
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x1c0);
                    /* try { // try from 00bcbdfc to 00ccbf0f has its CatchHandler @ 00bcbdbc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbda0"></a> `00bcbda0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbda4"></a> `00bcbda4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbda8"></a> `00bcbda8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbdac"></a> `00bcbdac` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcbdb0"></a> `00bcbdb0` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00bcbdb4"></a> `00bcbdb4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcbdb8"></a> `00bcbdb8` | `b4 62 00 91` | add x20,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bcbdbc"></a> `00bcbdbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbdc0"></a> `00bcbdc0` | `44 3b 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbdc4"></a> `00bcbdc4` | `b5 32 40 f9` | ldr x21,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bcbdc8"></a> `00bcbdc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbdcc"></a> `00bcbdcc` | `45 3b 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbdd0"></a> `00bcbdd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbdd4"></a> `00bcbdd4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcbdd8"></a> `00bcbdd8` | `da 3b 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbddc"></a> `00bcbddc` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcbde0"></a> `00bcbde0` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbde4"></a> `00bcbde4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbde8"></a> `00bcbde8` | `3e 3c 02 94` | bl 0x00c5aee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbdec"></a> `00bcbdec` | `a1 02 07 91` | add x1,x21,#0x1c0 | `FALL_THROUGH`
<a id="insn-00bcbdf0"></a> `00bcbdf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbdf4"></a> `00bcbdf4` | `0b 3c 02 94` | bl 0x00c5ae20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbdf8"></a> `00bcbdf8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbdfc"></a> `00bcbdfc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe00"></a> `00bcbe00` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbe04"></a> `00bcbe04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbda0`](#insn-00bcbda0) 範囲 `[['00bcbda0', '00bcbdbb']]`
  - `FALL_THROUGH` [`00bcbdb8`](#insn-00bcbdb8) → [`00bcbdbc`](#insn-00bcbdbc)
- ブロック [`00bcbdbc`](#insn-00bcbdbc) 範囲 `[['00bcbdbc', '00bcbdf3']]`
  - `FALL_THROUGH` [`00bcbdf0`](#insn-00bcbdf0) → [`00bcbdf4`](#insn-00bcbdf4)
- ブロック [`00bcbdf4`](#insn-00bcbdf4) 範囲 `[['00bcbdf4', '00bcbdfb']]`
  - `FALL_THROUGH` [`00bcbdf8`](#insn-00bcbdf8) → [`00bcbdfc`](#insn-00bcbdfc)
- ブロック [`00bcbdfc`](#insn-00bcbdfc) 範囲 `[['00bcbdfc', '00bcbe07']]`

## 命令位置別の参照

- [`00bcbda0`](#insn-00bcbda0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbda4`](#insn-00bcbda4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbda8`](#insn-00bcbda8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdc0`](#insn-00bcbdc0) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdcc`](#insn-00bcbdcc) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdd8`](#insn-00bcbdd8) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bcbde8`](#insn-00bcbde8) → [`00c5aee0`](../00c5a/00c5aee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aee0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdf4`](#insn-00bcbdf4) → [`00c5ae20`](../00c5a/00c5ae20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae20` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdf8`](#insn-00bcbdf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdfc`](#insn-00bcbdfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbda0`](#insn-00bcbda0)

~~~json
{
  "source": "00bcbda0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbda4`](#insn-00bcbda4)

~~~json
{
  "source": "00bcbda4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbda8`](#insn-00bcbda8)

~~~json
{
  "source": "00bcbda8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdc0`](#insn-00bcbdc0)

~~~json
{
  "source": "00bcbdc0",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbdcc`](#insn-00bcbdcc)

~~~json
{
  "source": "00bcbdcc",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbdd8`](#insn-00bcbdd8)

~~~json
{
  "source": "00bcbdd8",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbde8`](#insn-00bcbde8)

~~~json
{
  "source": "00bcbde8",
  "target": "00c5aee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbdf4`](#insn-00bcbdf4)

~~~json
{
  "source": "00bcbdf4",
  "target": "00c5ae20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbdf8`](#insn-00bcbdf8)

~~~json
{
  "source": "00bcbdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdfc`](#insn-00bcbdfc)

~~~json
{
  "source": "00bcbdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
