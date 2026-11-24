# 00bca2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc9e84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-4cf9cf1ba9c9901db9ba197a2f7f7799)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bca348`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca348.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0010.md#compare-d8dc883a4028403bc1fcdda7f82180a9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bca2ac",
  "name": "_ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSEOS1_",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c29da121be257e8f80aac953bcd30e3dd611c3707abfa79076ff41e08d23396",
  "source_text_sha256": "9c29da121be257e8f80aac953bcd30e3dd611c3707abfa79076ff41e08d23396",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bca2ac",
        "00bca323"
      ]
    ],
    "bytes_sha256": "691c1e386b82214c36489ada5a35bb50b8f1775e6b918fc80dfa1493bdb94dc6",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac10](../00c5a/00c5ac10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 909 bytes

~~~c

long _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSEOS1_(long param_1,long param_2)

{
  long lVar1;
  
  if (param_1 != param_2) {
    if (*(long *)(param_2 + 8) != 0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(*(long *)(param_2 + 8) + 0x138,param_2);
    }
    if (*(long *)(param_1 + 8) != 0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(*(long *)(param_1 + 8) + 0x138,param_1);
    }
    lVar1 = *(long *)(param_2 + 8);
    *(undefined8 *)(param_1 + 0x10) = *(undefined8 *)(param_2 + 0x10);
    *(long *)(param_1 + 8) = lVar1;
    if (lVar1 != 0) {
      _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E
                (lVar1 + 0x138,param_1,
                 PTR__ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv_00c9b920
                );
    }
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bca2ac"></a> `00bca2ac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bca2b0"></a> `00bca2b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca2b4"></a> `00bca2b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bca2b8"></a> `00bca2b8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bca2bc"></a> `00bca2bc` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bca2c0"></a> `00bca2c0` | `a0 02 00 54` | b.eq 0x00bca314 | `CONDITIONAL_JUMP`
<a id="insn-00bca2c4"></a> `00bca2c4` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bca2c8"></a> `00bca2c8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bca2cc"></a> `00bca2cc` | `88 00 00 b4` | cbz x8,0x00bca2dc | `CONDITIONAL_JUMP`
<a id="insn-00bca2d0"></a> `00bca2d0` | `00 e1 04 91` | add x0,x8,#0x138 | `FALL_THROUGH`
<a id="insn-00bca2d4"></a> `00bca2d4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bca2d8"></a> `00bca2d8` | `4e 42 02 94` | bl 0x00c5ac10 | `UNCONDITIONAL_CALL`
<a id="insn-00bca2dc"></a> `00bca2dc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca2e0"></a> `00bca2e0` | `88 00 00 b4` | cbz x8,0x00bca2f0 | `CONDITIONAL_JUMP`
<a id="insn-00bca2e4"></a> `00bca2e4` | `00 e1 04 91` | add x0,x8,#0x138 | `FALL_THROUGH`
<a id="insn-00bca2e8"></a> `00bca2e8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bca2ec"></a> `00bca2ec` | `49 42 02 94` | bl 0x00c5ac10 | `UNCONDITIONAL_CALL`
<a id="insn-00bca2f0"></a> `00bca2f0` | `80 82 c0 3c` | ldur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bca2f4"></a> `00bca2f4` | `08 00 66 9e` | fmov x8,d0 | `FALL_THROUGH`
<a id="insn-00bca2f8"></a> `00bca2f8` | `60 82 80 3c` | stur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca2fc"></a> `00bca2fc` | `c8 00 00 b4` | cbz x8,0x00bca314 | `CONDITIONAL_JUMP`
<a id="insn-00bca300"></a> `00bca300` | `82 06 00 b0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bca304"></a> `00bca304` | `42 90 44 f9` | ldr x2,[x2, #0x920] | `FALL_THROUGH`
<a id="insn-00bca308"></a> `00bca308` | `00 e1 04 91` | add x0,x8,#0x138 | `FALL_THROUGH`
<a id="insn-00bca30c"></a> `00bca30c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bca310"></a> `00bca310` | `3c 42 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bca314"></a> `00bca314` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca318"></a> `00bca318` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bca31c"></a> `00bca31c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bca320"></a> `00bca320` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bca2ac`](#insn-00bca2ac) 範囲 `[['00bca2ac', '00bca2c3']]`
  - `CONDITIONAL_JUMP` [`00bca2c0`](#insn-00bca2c0) → [`00bca314`](#insn-00bca314)
  - `FALL_THROUGH` [`00bca2c0`](#insn-00bca2c0) → [`00bca2c4`](#insn-00bca2c4)
- ブロック [`00bca2c4`](#insn-00bca2c4) 範囲 `[['00bca2c4', '00bca2cf']]`
  - `CONDITIONAL_JUMP` [`00bca2cc`](#insn-00bca2cc) → [`00bca2dc`](#insn-00bca2dc)
  - `FALL_THROUGH` [`00bca2cc`](#insn-00bca2cc) → [`00bca2d0`](#insn-00bca2d0)
- ブロック [`00bca2d0`](#insn-00bca2d0) 範囲 `[['00bca2d0', '00bca2db']]`
  - `FALL_THROUGH` [`00bca2d8`](#insn-00bca2d8) → [`00bca2dc`](#insn-00bca2dc)
- ブロック [`00bca2dc`](#insn-00bca2dc) 範囲 `[['00bca2dc', '00bca2e3']]`
  - `CONDITIONAL_JUMP` [`00bca2e0`](#insn-00bca2e0) → [`00bca2f0`](#insn-00bca2f0)
  - `FALL_THROUGH` [`00bca2e0`](#insn-00bca2e0) → [`00bca2e4`](#insn-00bca2e4)
- ブロック [`00bca2e4`](#insn-00bca2e4) 範囲 `[['00bca2e4', '00bca2ef']]`
  - `FALL_THROUGH` [`00bca2ec`](#insn-00bca2ec) → [`00bca2f0`](#insn-00bca2f0)
- ブロック [`00bca2f0`](#insn-00bca2f0) 範囲 `[['00bca2f0', '00bca2ff']]`
  - `CONDITIONAL_JUMP` [`00bca2fc`](#insn-00bca2fc) → [`00bca314`](#insn-00bca314)
  - `FALL_THROUGH` [`00bca2fc`](#insn-00bca2fc) → [`00bca300`](#insn-00bca300)
- ブロック [`00bca300`](#insn-00bca300) 範囲 `[['00bca300', '00bca313']]`
  - `FALL_THROUGH` [`00bca310`](#insn-00bca310) → [`00bca314`](#insn-00bca314)
- ブロック [`00bca314`](#insn-00bca314) 範囲 `[['00bca314', '00bca323']]`

## 命令位置別の参照

- [`00bca2ac`](#insn-00bca2ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2b0`](#insn-00bca2b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2c0`](#insn-00bca2c0) → [`00bca314`](#insn-00bca314) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2cc`](#insn-00bca2cc) → [`00bca2dc`](#insn-00bca2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2d8`](#insn-00bca2d8) → [`00c5ac10`](../00c5a/00c5ac10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac10` · 推定シンボル `None` · 推定型 `None`
- [`00bca2e0`](#insn-00bca2e0) → [`00bca2f0`](#insn-00bca2f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca2ec`](#insn-00bca2ec) → [`00c5ac10`](../00c5a/00c5ac10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac10` · 推定シンボル `None` · 推定型 `None`
- [`00bca2fc`](#insn-00bca2fc) → [`00bca314`](#insn-00bca314) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca304`](#insn-00bca304) → `00c9b920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bca304`](#insn-00bca304) → [`00bca360`](00bca360.md) · `PARAM` · `ANALYSIS` · 関数 `00bca360` · 推定シンボル `_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv` · 推定型 `None`
- [`00bca310`](#insn-00bca310) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bca314`](#insn-00bca314) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bca2ac`](#insn-00bca2ac)

~~~json
{
  "source": "00bca2ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2b0`](#insn-00bca2b0)

~~~json
{
  "source": "00bca2b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2c0`](#insn-00bca2c0)

~~~json
{
  "source": "00bca2c0",
  "target": "00bca314",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2cc`](#insn-00bca2cc)

~~~json
{
  "source": "00bca2cc",
  "target": "00bca2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2d8`](#insn-00bca2d8)

~~~json
{
  "source": "00bca2d8",
  "target": "00c5ac10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca2e0`](#insn-00bca2e0)

~~~json
{
  "source": "00bca2e0",
  "target": "00bca2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca2ec`](#insn-00bca2ec)

~~~json
{
  "source": "00bca2ec",
  "target": "00c5ac10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca2fc`](#insn-00bca2fc)

~~~json
{
  "source": "00bca2fc",
  "target": "00bca314",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca304`](#insn-00bca304)

~~~json
{
  "source": "00bca304",
  "target": "00c9b920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b920",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bca304`](#insn-00bca304)

~~~json
{
  "source": "00bca304",
  "target": "00bca360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca310`](#insn-00bca310)

~~~json
{
  "source": "00bca310",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca314`](#insn-00bca314)

~~~json
{
  "source": "00bca314",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
