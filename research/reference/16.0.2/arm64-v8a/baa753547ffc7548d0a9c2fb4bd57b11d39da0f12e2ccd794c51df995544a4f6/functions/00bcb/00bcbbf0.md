# 00bcbbf0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbb54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-338638432d84b6272d3fd8559c3643c8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bccbe4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccbe4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-63d73fc7f196e06a3d05177ea56ce4a9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbbf0",
  "name": "_ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b8677346db19ae62fbec0b9e49bd04da95788d45f4ddc1b30d9459e0d46ab31",
  "source_text_sha256": "8b8677346db19ae62fbec0b9e49bd04da95788d45f4ddc1b30d9459e0d46ab31",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbbf0",
        "00bcbc57"
      ]
    ],
    "bytes_sha256": "aaa3ddf523c2175e844465636275dd90fb00bbfaab95236df80ddeaffeb88013",
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
                    /* try { // try from 00bcbc38 to 00ccbc43 has its CatchHandler @ 00bcbc9c */
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bcbc44 to 00ccbcc3 has its CatchHandler @ 00bcbbcc */
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbbf0"></a> `00bcbbf0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbbf4"></a> `00bcbbf4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbf8"></a> `00bcbbf8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbfc"></a> `00bcbbfc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcbc00"></a> `00bcbc00` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00bcbc04"></a> `00bcbc04` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcbc08"></a> `00bcbc08` | `b4 62 00 91` | add x20,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bcbc0c"></a> `00bcbc0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbc10"></a> `00bcbc10` | `b0 3b 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc14"></a> `00bcbc14` | `b5 32 40 f9` | ldr x21,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bcbc18"></a> `00bcbc18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbc1c"></a> `00bcbc1c` | `b1 3b 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc20"></a> `00bcbc20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbc24"></a> `00bcbc24` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcbc28"></a> `00bcbc28` | `46 3c 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc2c"></a> `00bcbc2c` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcbc30"></a> `00bcbc30` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbc34"></a> `00bcbc34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbc38"></a> `00bcbc38` | `aa 3c 02 94` | bl 0x00c5aee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc3c"></a> `00bcbc3c` | `a1 02 03 91` | add x1,x21,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbc40"></a> `00bcbc40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbc44"></a> `00bcbc44` | `77 3c 02 94` | bl 0x00c5ae20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc48"></a> `00bcbc48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbc4c"></a> `00bcbc4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc50"></a> `00bcbc50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbc54"></a> `00bcbc54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbbf0`](#insn-00bcbbf0) 範囲 `[['00bcbbf0', '00bcbc37']]`
  - `FALL_THROUGH` [`00bcbc34`](#insn-00bcbc34) → [`00bcbc38`](#insn-00bcbc38)
- ブロック [`00bcbc38`](#insn-00bcbc38) 範囲 `[['00bcbc38', '00bcbc43']]`
  - `FALL_THROUGH` [`00bcbc40`](#insn-00bcbc40) → [`00bcbc44`](#insn-00bcbc44)
- ブロック [`00bcbc44`](#insn-00bcbc44) 範囲 `[['00bcbc44', '00bcbc57']]`

## 命令位置別の参照

- [`00bcbbf0`](#insn-00bcbbf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf4`](#insn-00bcbbf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf8`](#insn-00bcbbf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc10`](#insn-00bcbc10) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc1c`](#insn-00bcbc1c) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc28`](#insn-00bcbc28) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc38`](#insn-00bcbc38) → [`00c5aee0`](../00c5a/00c5aee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aee0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc44`](#insn-00bcbc44) → [`00c5ae20`](../00c5a/00c5ae20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae20` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc48`](#insn-00bcbc48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc4c`](#insn-00bcbc4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbbf0`](#insn-00bcbbf0)

~~~json
{
  "source": "00bcbbf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf4`](#insn-00bcbbf4)

~~~json
{
  "source": "00bcbbf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf8`](#insn-00bcbbf8)

~~~json
{
  "source": "00bcbbf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc10`](#insn-00bcbc10)

~~~json
{
  "source": "00bcbc10",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc1c`](#insn-00bcbc1c)

~~~json
{
  "source": "00bcbc1c",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc28`](#insn-00bcbc28)

~~~json
{
  "source": "00bcbc28",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc38`](#insn-00bcbc38)

~~~json
{
  "source": "00bcbc38",
  "target": "00c5aee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc44`](#insn-00bcbc44)

~~~json
{
  "source": "00bcbc44",
  "target": "00c5ae20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc48`](#insn-00bcbc48)

~~~json
{
  "source": "00bcbc48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc4c`](#insn-00bcbc4c)

~~~json
{
  "source": "00bcbc4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
