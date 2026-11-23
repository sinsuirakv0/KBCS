# 00bcb3cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcb304`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb304.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-9ff9a4ada5d036486218962e08dfbe60)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcb410`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-32d004b1e70c3c21b4e6a22fb2f0072d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb3cc",
  "name": "FUN_00bcb3cc",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "750c5d00bc3b008376f5ddbf8e8ca8ec7c78f4db047f6c910629352cb98fdfcb",
  "source_text_sha256": "750c5d00bc3b008376f5ddbf8e8ca8ec7c78f4db047f6c910629352cb98fdfcb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb3cc",
        "00bcb443"
      ]
    ],
    "bytes_sha256": "afc4d1ff024459ad1656f139b93c0c4f9a1ae99381b4c7087645fe55f8b4b01b",
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

- [00bbb158](../00bbb/00bbb158.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 557 bytes

~~~c

void FUN_00bcb3cc(long *param_1)

{
  long lVar1;
  long *__ptr;
  
  lVar1 = *param_1;
  if ((ulong)(*(long *)(lVar1 + 0x2a0) - *(long *)(lVar1 + 0x298) >> 3) < (ulong)param_1[1]) {
                    /* WARNING: Subroutine does not return */
    FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0xa4f,
                 &DAT_00296866);
  }
  __ptr = (long *)param_1[2];
  *(long *)(lVar1 + 0x2a0) = *(long *)(lVar1 + 0x298) + param_1[1] * 8;
  if (__ptr != param_1 + 5) {
    free(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb3cc"></a> `00bcb3cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcb3d0"></a> `00bcb3d0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bcb3d4"></a> `00bcb3d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcb3d8"></a> `00bcb3d8` | `09 28 40 a9` | ldp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00bcb3dc"></a> `00bcb3dc` | `28 51 41 f9` | ldr x8,[x9, #0x2a0] | `FALL_THROUGH`
<a id="insn-00bcb3e0"></a> `00bcb3e0` | `2b 4d 41 f9` | ldr x11,[x9, #0x298] | `FALL_THROUGH`
<a id="insn-00bcb3e4"></a> `00bcb3e4` | `08 01 0b cb` | sub x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00bcb3e8"></a> `00bcb3e8` | `5f 0d 88 eb` | cmp x10,x8, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcb3ec"></a> `00bcb3ec` | `c8 01 00 54` | b.hi 0x00bcb424 | `CONDITIONAL_JUMP`
<a id="insn-00bcb3f0"></a> `00bcb3f0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb3f4"></a> `00bcb3f4` | `6a 0d 0a 8b` | add x10,x11,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcb3f8"></a> `00bcb3f8` | `0b a0 00 91` | add x11,x0,#0x28 | `FALL_THROUGH`
<a id="insn-00bcb3fc"></a> `00bcb3fc` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-00bcb400"></a> `00bcb400` | `2a 51 01 f9` | str x10,[x9, #0x2a0] | `FALL_THROUGH`
<a id="insn-00bcb404"></a> `00bcb404` | `a0 00 00 54` | b.eq 0x00bcb418 | `CONDITIONAL_JUMP`
<a id="insn-00bcb408"></a> `00bcb408` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcb40c"></a> `00bcb40c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bcb410"></a> `00bcb410` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcb414"></a> `00bcb414` | `eb 40 00 14` | b 0x00bdb7c0 | `CALL_TERMINATOR`
<a id="insn-00bcb418"></a> `00bcb418` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bcb41c"></a> `00bcb41c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcb420"></a> `00bcb420` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcb424"></a> `00bcb424` | `20 b6 ff d0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bcb428"></a> `00bcb428` | `00 f0 1f 91` | add x0,x0,#0x7fc | `FALL_THROUGH`
<a id="insn-00bcb42c"></a> `00bcb42c` | `a1 b6 ff f0` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bcb430"></a> `00bcb430` | `21 28 04 91` | add x1,x1,#0x10a | `FALL_THROUGH`
<a id="insn-00bcb434"></a> `00bcb434` | `43 b6 ff f0` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00bcb438"></a> `00bcb438` | `63 98 21 91` | add x3,x3,#0x866 | `FALL_THROUGH`
<a id="insn-00bcb43c"></a> `00bcb43c` | `e2 49 81 52` | mov w2,#0xa4f | `FALL_THROUGH`
<a id="insn-00bcb440"></a> `00bcb440` | `46 bf ff 97` | bl 0x00bbb158 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb3cc`](#insn-00bcb3cc) 範囲 `[['00bcb3cc', '00bcb3ef']]`
  - `CONDITIONAL_JUMP` [`00bcb3ec`](#insn-00bcb3ec) → [`00bcb424`](#insn-00bcb424)
  - `FALL_THROUGH` [`00bcb3ec`](#insn-00bcb3ec) → [`00bcb3f0`](#insn-00bcb3f0)
- ブロック [`00bcb3f0`](#insn-00bcb3f0) 範囲 `[['00bcb3f0', '00bcb407']]`
  - `CONDITIONAL_JUMP` [`00bcb404`](#insn-00bcb404) → [`00bcb418`](#insn-00bcb418)
  - `FALL_THROUGH` [`00bcb404`](#insn-00bcb404) → [`00bcb408`](#insn-00bcb408)
- ブロック [`00bcb408`](#insn-00bcb408) 範囲 `[['00bcb408', '00bcb417']]`
- ブロック [`00bcb418`](#insn-00bcb418) 範囲 `[['00bcb418', '00bcb423']]`
- ブロック [`00bcb424`](#insn-00bcb424) 範囲 `[['00bcb424', '00bcb443']]`

## 命令位置別の参照

- [`00bcb3d0`](#insn-00bcb3d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb3ec`](#insn-00bcb3ec) → [`00bcb424`](#insn-00bcb424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb404`](#insn-00bcb404) → [`00bcb418`](#insn-00bcb418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb40c`](#insn-00bcb40c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb414`](#insn-00bcb414) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb418`](#insn-00bcb418) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb428`](#insn-00bcb428) → `002917fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcb430`](#insn-00bcb430) → `002a210a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcb438`](#insn-00bcb438) → `00296866`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcb440`](#insn-00bcb440) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb3d0`](#insn-00bcb3d0)

~~~json
{
  "source": "00bcb3d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb3ec`](#insn-00bcb3ec)

~~~json
{
  "source": "00bcb3ec",
  "target": "00bcb424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb404`](#insn-00bcb404)

~~~json
{
  "source": "00bcb404",
  "target": "00bcb418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb40c`](#insn-00bcb40c)

~~~json
{
  "source": "00bcb40c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb414`](#insn-00bcb414)

~~~json
{
  "source": "00bcb414",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb418`](#insn-00bcb418)

~~~json
{
  "source": "00bcb418",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb428`](#insn-00bcb428)

~~~json
{
  "source": "00bcb428",
  "target": "002917fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917fc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "25733a25643a20257300",
  "capture_start": "002917fc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcb430`](#insn-00bcb430)

~~~json
{
  "source": "00bcb430",
  "target": "002a210a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a210a",
  "offset": 0,
  "size": 58,
  "datatype": "string",
  "bytes": "6f75742f6c6c766d2d70726f6a6563742f6c69626378786162692f7372632f64",
  "capture_start": "002a210a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcb438`](#insn-00bcb438)

~~~json
{
  "source": "00bcb438",
  "target": "00296866",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296866",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "00296866",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcb440`](#insn-00bcb440)

~~~json
{
  "source": "00bcb440",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
