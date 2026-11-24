# 00bccbe4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbbf0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbbf0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-63d73fc7f196e06a3d05177ea56ce4a9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccbe4",
  "name": "_ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41f3fd47da22ca213fa72c117123d81561bf718ec543db87b647d60f26555c73",
  "source_text_sha256": "41f3fd47da22ca213fa72c117123d81561bf718ec543db87b647d60f26555c73",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccbe4",
        "00bccc4b"
      ]
    ],
    "bytes_sha256": "dfb7458283245afdf954f9310989760b602d8accaddd5a5533f14f853a03abd3",
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

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5bdf0](../00c5b/00c5bdf0.md)
- [00c5beb0](../00c5b/00c5beb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 714 bytes

~~~c

void _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv
               (long param_1,long *param_2)

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
                    /* try { // try from 00bccc2c to 00cccc37 has its CatchHandler @ 00bccc90 */
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bccc38 to 00ccccb7 has its CatchHandler @ 00bccbc0 */
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccbe4"></a> `00bccbe4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bccbe8"></a> `00bccbe8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccbec"></a> `00bccbec` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccbf0"></a> `00bccbf0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bccbf4"></a> `00bccbf4` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00bccbf8"></a> `00bccbf8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bccbfc"></a> `00bccbfc` | `b4 62 00 91` | add x20,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bccc00"></a> `00bccc00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bccc04"></a> `00bccc04` | `a7 3b 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc08"></a> `00bccc08` | `b5 32 40 f9` | ldr x21,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bccc0c"></a> `00bccc0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bccc10"></a> `00bccc10` | `a8 3b 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc14"></a> `00bccc14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccc18"></a> `00bccc18` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bccc1c"></a> `00bccc1c` | `3d 3c 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc20"></a> `00bccc20` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bccc24"></a> `00bccc24` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bccc28"></a> `00bccc28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bccc2c"></a> `00bccc2c` | `a1 3c 02 94` | bl 0x00c5beb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc30"></a> `00bccc30` | `a1 02 03 91` | add x1,x21,#0xc0 | `FALL_THROUGH`
<a id="insn-00bccc34"></a> `00bccc34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccc38"></a> `00bccc38` | `6e 3c 02 94` | bl 0x00c5bdf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc3c"></a> `00bccc3c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccc40"></a> `00bccc40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccc44"></a> `00bccc44` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bccc48"></a> `00bccc48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccbe4`](#insn-00bccbe4) 範囲 `[['00bccbe4', '00bccc2b']]`
  - `FALL_THROUGH` [`00bccc28`](#insn-00bccc28) → [`00bccc2c`](#insn-00bccc2c)
- ブロック [`00bccc2c`](#insn-00bccc2c) 範囲 `[['00bccc2c', '00bccc37']]`
  - `FALL_THROUGH` [`00bccc34`](#insn-00bccc34) → [`00bccc38`](#insn-00bccc38)
- ブロック [`00bccc38`](#insn-00bccc38) 範囲 `[['00bccc38', '00bccc4b']]`

## 命令位置別の参照

- [`00bccbe4`](#insn-00bccbe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbe8`](#insn-00bccbe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbec`](#insn-00bccbec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccc04`](#insn-00bccc04) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bccc10`](#insn-00bccc10) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bccc1c`](#insn-00bccc1c) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bccc2c`](#insn-00bccc2c) → [`00c5beb0`](../00c5b/00c5beb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5beb0` · 推定シンボル `None` · 推定型 `None`
- [`00bccc38`](#insn-00bccc38) → [`00c5bdf0`](../00c5b/00c5bdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdf0` · 推定シンボル `None` · 推定型 `None`
- [`00bccc3c`](#insn-00bccc3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccc40`](#insn-00bccc40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccbe4`](#insn-00bccbe4)

~~~json
{
  "source": "00bccbe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbe8`](#insn-00bccbe8)

~~~json
{
  "source": "00bccbe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbec`](#insn-00bccbec)

~~~json
{
  "source": "00bccbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccc04`](#insn-00bccc04)

~~~json
{
  "source": "00bccc04",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc10`](#insn-00bccc10)

~~~json
{
  "source": "00bccc10",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc1c`](#insn-00bccc1c)

~~~json
{
  "source": "00bccc1c",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc2c`](#insn-00bccc2c)

~~~json
{
  "source": "00bccc2c",
  "target": "00c5beb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc38`](#insn-00bccc38)

~~~json
{
  "source": "00bccc38",
  "target": "00c5bdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc3c`](#insn-00bccc3c)

~~~json
{
  "source": "00bccc3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccc40`](#insn-00bccc40)

~~~json
{
  "source": "00bccc40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
