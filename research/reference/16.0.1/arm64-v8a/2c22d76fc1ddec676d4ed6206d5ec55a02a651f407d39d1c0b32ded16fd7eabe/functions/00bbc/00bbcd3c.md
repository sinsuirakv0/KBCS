# 00bbcd3c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbc914`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc914.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-feabe51bc43a338848683d728e64fe36)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbcdd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcdd8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-3d1a90df260122044b5f3a7087af8a26)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcd3c",
  "name": "_ZN8firebase9messaging18GetTokenLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e2fc3f9cf05b9428e7938da469d2a7a1857f3ad7cdd4f75b7cad540dae43a22",
  "source_text_sha256": "8e2fc3f9cf05b9428e7938da469d2a7a1857f3ad7cdd4f75b7cad540dae43a22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcd3c",
        "00bbcde3"
      ]
    ],
    "bytes_sha256": "7ab52a552bd71b79681a679ab1a6583bef93b863c45b84f58a6dacb85599742c",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
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
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ad50](../00c5a/00c5ad50.md)
- [00c5ae10](../00c5a/00c5ae10.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5d270](../00c5d/00c5d270.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1070 bytes

~~~c

void _ZN8firebase9messaging18GetTokenLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_01126360 == 0) {
                    /* try { // try from 00bbcda8 to 00cbcdaf has its CatchHandler @ 00bbce7c */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bbcdc4 to 00cbcdcb has its CatchHandler @ 00bbce74 */
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  }
                    /* try { // try from 00bbcddc to 00cbcde3 has its CatchHandler @ 00bbce70 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcd3c"></a> `00bbcd3c` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbcd40"></a> `00bbcd40` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcd44"></a> `00bbcd44` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcd48"></a> `00bbcd48` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbcd4c"></a> `00bbcd4c` | `49 2b 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcd50"></a> `00bbcd50` | `29 b1 41 f9` | ldr x9,[x9, #0x360] | `FALL_THROUGH`
<a id="insn-00bbcd54"></a> `00bbcd54` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bbcd58"></a> `00bbcd58` | `89 02 00 b4` | cbz x9,0x00bbcda8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd5c"></a> `00bbcd5c` | `45 81 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd60"></a> `00bbcd60` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcd64"></a> `00bbcd64` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbcd68"></a> `00bbcd68` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcd6c"></a> `00bbcd6c` | `25 77 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd70"></a> `00bbcd70` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcd74"></a> `00bbcd74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcd78"></a> `00bbcd78` | `26 77 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd7c"></a> `00bbcd7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd80"></a> `00bbcd80` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbcd84"></a> `00bbcd84` | `bb 77 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd88"></a> `00bbcd88` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcd8c"></a> `00bbcd8c` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcd90"></a> `00bbcd90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcd94"></a> `00bbcd94` | `1f 78 02 94` | bl 0x00c5ae10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd98"></a> `00bbcd98` | `c1 02 03 91` | add x1,x22,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbcd9c"></a> `00bbcd9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcda0"></a> `00bbcda0` | `ec 77 02 94` | bl 0x00c5ad50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcda4"></a> `00bbcda4` | `0c 00 00 14` | b 0x00bbcdd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcda8"></a> `00bbcda8` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbcdac"></a> `00bbcdac` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbcdb0"></a> `00bbcdb0` | `94 78 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdb4"></a> `00bbcdb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcdb8"></a> `00bbcdb8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbcdbc"></a> `00bbcdbc` | `ad 77 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdc0"></a> `00bbcdc0` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcdc4"></a> `00bbcdc4` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcdc8"></a> `00bbcdc8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbcdcc"></a> `00bbcdcc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbcdd0"></a> `00bbcdd0` | `84 77 02 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdd4"></a> `00bbcdd4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcdd8"></a> `00bbcdd8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcddc"></a> `00bbcddc` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbcde0"></a> `00bbcde0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcd3c`](#insn-00bbcd3c) 範囲 `[['00bbcd3c', '00bbcd5b']]`
  - `CONDITIONAL_JUMP` [`00bbcd58`](#insn-00bbcd58) → [`00bbcda8`](#insn-00bbcda8)
  - `FALL_THROUGH` [`00bbcd58`](#insn-00bbcd58) → [`00bbcd5c`](#insn-00bbcd5c)
- ブロック [`00bbcd5c`](#insn-00bbcd5c) 範囲 `[['00bbcd5c', '00bbcda7']]`
  - `UNCONDITIONAL_JUMP` [`00bbcda4`](#insn-00bbcda4) → [`00bbcdd4`](#insn-00bbcdd4)
- ブロック [`00bbcda8`](#insn-00bbcda8) 範囲 `[['00bbcda8', '00bbcdc3']]`
  - `FALL_THROUGH` [`00bbcdc0`](#insn-00bbcdc0) → [`00bbcdc4`](#insn-00bbcdc4)
- ブロック [`00bbcdc4`](#insn-00bbcdc4) 範囲 `[['00bbcdc4', '00bbcdd3']]`
  - `FALL_THROUGH` [`00bbcdd0`](#insn-00bbcdd0) → [`00bbcdd4`](#insn-00bbcdd4)
- ブロック [`00bbcdd4`](#insn-00bbcdd4) 範囲 `[['00bbcdd4', '00bbcddb']]`
  - `FALL_THROUGH` [`00bbcdd8`](#insn-00bbcdd8) → [`00bbcddc`](#insn-00bbcddc)
- ブロック [`00bbcddc`](#insn-00bbcddc) 範囲 `[['00bbcddc', '00bbcde3']]`

## 命令位置別の参照

- [`00bbcd3c`](#insn-00bbcd3c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd40`](#insn-00bbcd40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd44`](#insn-00bbcd44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd50`](#insn-00bbcd50) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcd58`](#insn-00bbcd58) → [`00bbcda8`](#insn-00bbcda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd5c`](#insn-00bbcd5c) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd6c`](#insn-00bbcd6c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd78`](#insn-00bbcd78) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd84`](#insn-00bbcd84) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd94`](#insn-00bbcd94) → [`00c5ae10`](../00c5a/00c5ae10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcda0`](#insn-00bbcda0) → [`00c5ad50`](../00c5a/00c5ad50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad50` · 推定シンボル `None` · 推定型 `None`
- [`00bbcda4`](#insn-00bbcda4) → [`00bbcdd4`](#insn-00bbcdd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdac`](#insn-00bbcdac) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcdb0`](#insn-00bbcdb0) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdbc`](#insn-00bbcdbc) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdd0`](#insn-00bbcdd0) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdd4`](#insn-00bbcdd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdd8`](#insn-00bbcdd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcd3c`](#insn-00bbcd3c)

~~~json
{
  "source": "00bbcd3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd40`](#insn-00bbcd40)

~~~json
{
  "source": "00bbcd40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd44`](#insn-00bbcd44)

~~~json
{
  "source": "00bbcd44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd50`](#insn-00bbcd50)

~~~json
{
  "source": "00bbcd50",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcd58`](#insn-00bbcd58)

~~~json
{
  "source": "00bbcd58",
  "target": "00bbcda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd5c`](#insn-00bbcd5c)

~~~json
{
  "source": "00bbcd5c",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd6c`](#insn-00bbcd6c)

~~~json
{
  "source": "00bbcd6c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd78`](#insn-00bbcd78)

~~~json
{
  "source": "00bbcd78",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd84`](#insn-00bbcd84)

~~~json
{
  "source": "00bbcd84",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd94`](#insn-00bbcd94)

~~~json
{
  "source": "00bbcd94",
  "target": "00c5ae10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcda0`](#insn-00bbcda0)

~~~json
{
  "source": "00bbcda0",
  "target": "00c5ad50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcda4`](#insn-00bbcda4)

~~~json
{
  "source": "00bbcda4",
  "target": "00bbcdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdac`](#insn-00bbcdac)

~~~json
{
  "source": "00bbcdac",
  "target": "002a2915",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2915",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2915",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcdb0`](#insn-00bbcdb0)

~~~json
{
  "source": "00bbcdb0",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdbc`](#insn-00bbcdbc)

~~~json
{
  "source": "00bbcdbc",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdd0`](#insn-00bbcdd0)

~~~json
{
  "source": "00bbcdd0",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdd4`](#insn-00bbcdd4)

~~~json
{
  "source": "00bbcdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdd8`](#insn-00bbcdd8)

~~~json
{
  "source": "00bbcdd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
