# 00bfb3dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa3e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-da7d9cf4c56d3b649174963851f8a834)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb3dc",
  "name": "_ZNSt6__ndk111timed_mutex4lockEv",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d70b7dcaaeef944381f6fbfbe62dd59a057fe84765eb0022aa17f34dc3b2806",
  "source_text_sha256": "7d70b7dcaaeef944381f6fbfbe62dd59a057fe84765eb0022aa17f34dc3b2806",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb3dc",
        "00bfb467"
      ]
    ],
    "bytes_sha256": "6cc8d65f4b5a0332e4c6d0e38c70f267fa6a22e07a78543b4da60a0e2215dd13",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c591c0](../00c59/00c591c0.md)
- [00c59520](../00c59/00c59520.md)
- [00c5c740](../00c5c/00c5c740.md)
- [00c5c750](../00c5c/00c5c750.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 884 bytes

~~~c

ulong _ZNSt6__ndk111timed_mutex4lockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  uint uVar2;
  ulong uVar3;
  pthread_mutex_t *local_30;
  char local_28;
  
  local_28 = '\x01';
  local_30 = param_1;
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
  }
  if ((*(byte *)((long)param_1 + 0x58) & 1) == 0) {
    *(undefined1 *)((long)param_1 + 0x58) = 1;
  }
  else {
    do {
      uVar3 = _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE
                        (param_1 + 1,&local_30);
    } while ((*(byte *)((long)param_1 + 0x58) & 1) != 0);
    *(undefined1 *)((long)param_1 + 0x58) = 1;
    if (local_28 == '\0') {
      return uVar3;
    }
  }
  uVar2 = pthread_mutex_unlock(local_30);
  return (ulong)uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb3dc"></a> `00bfb3dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb3e0"></a> `00bfb3e0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfb3e4"></a> `00bfb3e4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb3e8"></a> `00bfb3e8` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb3ec"></a> `00bfb3ec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfb3f0"></a> `00bfb3f0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb3f4"></a> `00bfb3f4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb3f8"></a> `00bfb3f8` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00bfb3fc"></a> `00bfb3fc` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfb400"></a> `00bfb400` | `d0 84 01 94` | bl 0x00c5c740 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb404"></a> `00bfb404` | `c0 02 00 35` | cbnz w0,0x00bfb45c | `CONDITIONAL_JUMP`
<a id="insn-00bfb408"></a> `00bfb408` | `68 62 41 39` | ldrb w8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb40c"></a> `00bfb40c` | `68 01 00 36` | tbz w8,#0x0,0x00bfb438 | `CONDITIONAL_JUMP`
<a id="insn-00bfb410"></a> `00bfb410` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfb414"></a> `00bfb414` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bfb418"></a> `00bfb418` | `42 78 01 94` | bl 0x00c59520 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb41c"></a> `00bfb41c` | `68 62 41 39` | ldrb w8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb420"></a> `00bfb420` | `88 ff 07 37` | tbnz w8,#0x0,0x00bfb410 | `CONDITIONAL_JUMP`
<a id="insn-00bfb424"></a> `00bfb424` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfb428"></a> `00bfb428` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb42c"></a> `00bfb42c` | `69 62 01 39` | strb w9,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb430"></a> `00bfb430` | `88 00 00 35` | cbnz w8,0x00bfb440 | `CONDITIONAL_JUMP`
<a id="insn-00bfb434"></a> `00bfb434` | `05 00 00 14` | b 0x00bfb448 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfb438"></a> `00bfb438` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb43c"></a> `00bfb43c` | `68 62 01 39` | strb w8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb440"></a> `00bfb440` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00bfb444"></a> `00bfb444` | `c3 84 01 94` | bl 0x00c5c750 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb448"></a> `00bfb448` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb44c"></a> `00bfb44c` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb450"></a> `00bfb450` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfb454"></a> `00bfb454` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb458"></a> `00bfb458` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb45c"></a> `00bfb45c` | `a1 b5 ff d0` | adrp x1,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bfb460"></a> `00bfb460` | `21 64 20 91` | add x1,x1,#0x819 | `FALL_THROUGH`
<a id="insn-00bfb464"></a> `00bfb464` | `57 77 01 94` | bl 0x00c591c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb3dc`](#insn-00bfb3dc) 範囲 `[['00bfb3dc', '00bfb407']]`
  - `CONDITIONAL_JUMP` [`00bfb404`](#insn-00bfb404) → [`00bfb45c`](#insn-00bfb45c)
  - `FALL_THROUGH` [`00bfb404`](#insn-00bfb404) → [`00bfb408`](#insn-00bfb408)
- ブロック [`00bfb408`](#insn-00bfb408) 範囲 `[['00bfb408', '00bfb40f']]`
  - `CONDITIONAL_JUMP` [`00bfb40c`](#insn-00bfb40c) → [`00bfb438`](#insn-00bfb438)
  - `FALL_THROUGH` [`00bfb40c`](#insn-00bfb40c) → [`00bfb410`](#insn-00bfb410)
- ブロック [`00bfb410`](#insn-00bfb410) 範囲 `[['00bfb410', '00bfb423']]`
  - `CONDITIONAL_JUMP` [`00bfb420`](#insn-00bfb420) → [`00bfb410`](#insn-00bfb410)
  - `FALL_THROUGH` [`00bfb420`](#insn-00bfb420) → [`00bfb424`](#insn-00bfb424)
- ブロック [`00bfb424`](#insn-00bfb424) 範囲 `[['00bfb424', '00bfb433']]`
  - `CONDITIONAL_JUMP` [`00bfb430`](#insn-00bfb430) → [`00bfb440`](#insn-00bfb440)
  - `FALL_THROUGH` [`00bfb430`](#insn-00bfb430) → [`00bfb434`](#insn-00bfb434)
- ブロック [`00bfb434`](#insn-00bfb434) 範囲 `[['00bfb434', '00bfb437']]`
  - `UNCONDITIONAL_JUMP` [`00bfb434`](#insn-00bfb434) → [`00bfb448`](#insn-00bfb448)
- ブロック [`00bfb438`](#insn-00bfb438) 範囲 `[['00bfb438', '00bfb43f']]`
  - `FALL_THROUGH` [`00bfb43c`](#insn-00bfb43c) → [`00bfb440`](#insn-00bfb440)
- ブロック [`00bfb440`](#insn-00bfb440) 範囲 `[['00bfb440', '00bfb447']]`
  - `FALL_THROUGH` [`00bfb444`](#insn-00bfb444) → [`00bfb448`](#insn-00bfb448)
- ブロック [`00bfb448`](#insn-00bfb448) 範囲 `[['00bfb448', '00bfb45b']]`
- ブロック [`00bfb45c`](#insn-00bfb45c) 範囲 `[['00bfb45c', '00bfb467']]`

## 命令位置別の参照

- [`00bfb3e4`](#insn-00bfb3e4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3e8`](#insn-00bfb3e8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3f8`](#insn-00bfb3f8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3fc`](#insn-00bfb3fc) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb400`](#insn-00bfb400) → [`00c5c740`](../00c5c/00c5c740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c740` · 推定シンボル `None` · 推定型 `None`
- [`00bfb404`](#insn-00bfb404) → [`00bfb45c`](#insn-00bfb45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb40c`](#insn-00bfb40c) → [`00bfb438`](#insn-00bfb438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb418`](#insn-00bfb418) → [`00c59520`](../00c59/00c59520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59520` · 推定シンボル `None` · 推定型 `None`
- [`00bfb420`](#insn-00bfb420) → [`00bfb410`](#insn-00bfb410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb424`](#insn-00bfb424) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb430`](#insn-00bfb430) → [`00bfb440`](#insn-00bfb440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb434`](#insn-00bfb434) → [`00bfb448`](#insn-00bfb448) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb440`](#insn-00bfb440) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb444`](#insn-00bfb444) → [`00c5c750`](../00c5c/00c5c750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c750` · 推定シンボル `None` · 推定型 `None`
- [`00bfb448`](#insn-00bfb448) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb44c`](#insn-00bfb44c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb460`](#insn-00bfb460) → `002b1819`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfb464`](#insn-00bfb464) → [`00c591c0`](../00c59/00c591c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c591c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb3e4`](#insn-00bfb3e4)

~~~json
{
  "source": "00bfb3e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3e8`](#insn-00bfb3e8)

~~~json
{
  "source": "00bfb3e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3f8`](#insn-00bfb3f8)

~~~json
{
  "source": "00bfb3f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3fc`](#insn-00bfb3fc)

~~~json
{
  "source": "00bfb3fc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb400`](#insn-00bfb400)

~~~json
{
  "source": "00bfb400",
  "target": "00c5c740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb404`](#insn-00bfb404)

~~~json
{
  "source": "00bfb404",
  "target": "00bfb45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb40c`](#insn-00bfb40c)

~~~json
{
  "source": "00bfb40c",
  "target": "00bfb438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb418`](#insn-00bfb418)

~~~json
{
  "source": "00bfb418",
  "target": "00c59520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb420`](#insn-00bfb420)

~~~json
{
  "source": "00bfb420",
  "target": "00bfb410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb424`](#insn-00bfb424)

~~~json
{
  "source": "00bfb424",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb430`](#insn-00bfb430)

~~~json
{
  "source": "00bfb430",
  "target": "00bfb440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb434`](#insn-00bfb434)

~~~json
{
  "source": "00bfb434",
  "target": "00bfb448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb440`](#insn-00bfb440)

~~~json
{
  "source": "00bfb440",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb444`](#insn-00bfb444)

~~~json
{
  "source": "00bfb444",
  "target": "00c5c750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb448`](#insn-00bfb448)

~~~json
{
  "source": "00bfb448",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb44c`](#insn-00bfb44c)

~~~json
{
  "source": "00bfb44c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb460`](#insn-00bfb460)

~~~json
{
  "source": "00bfb460",
  "target": "002b1819",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1819",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6d75746578206c6f636b206661696c656400",
  "capture_start": "002b1819",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfb464`](#insn-00bfb464)

~~~json
{
  "source": "00bfb464",
  "target": "00c591c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
