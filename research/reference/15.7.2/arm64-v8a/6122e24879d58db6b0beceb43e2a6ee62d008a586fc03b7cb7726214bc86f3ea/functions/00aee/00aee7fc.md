# 00aee7fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aee8c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-993734240b802d09e2c339bfdd2f62cb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aee7fc",
  "name": "FUN_00aee7fc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "127f3aecc5ccaf514eb262fa56069a8ddb38f2993ce75f5c89d721732e14817b",
  "source_text_sha256": "127f3aecc5ccaf514eb262fa56069a8ddb38f2993ce75f5c89d721732e14817b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aee7fc",
        "00aee883"
      ]
    ],
    "bytes_sha256": "b596dceb961d569f398a37e9018ff6c0a1790243acda371ae9e2a1d57f3b82ce",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00aee28c](../00aee/00aee28c.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 671 bytes

~~~c

void FUN_00aee7fc(long *param_1)

{
  void *__ptr;
  undefined8 *puVar1;
  undefined8 *puVar2;
  
  puVar2 = (undefined8 *)*DAT_010a09b0;
  puVar1 = DAT_010a09b0 + 1;
  if (puVar2 != (undefined8 *)*puVar1) {
    do {
      puVar1 = puVar2 + 1;
      (**(code **)(*param_1 + 0xb0))(param_1,*puVar2);
      puVar2 = puVar1;
    } while (puVar1 != (undefined8 *)DAT_010a09b0[1]);
    puVar1 = DAT_010a09b0 + 1;
  }
  puVar2 = DAT_010a09b0;
  if (DAT_010a09b0 != (undefined8 *)0x0) {
    __ptr = (void *)*DAT_010a09b0;
    if (__ptr != (void *)0x0) {
      *puVar1 = __ptr;
      _ZdlPv(__ptr);
    }
    _ZdlPv(puVar2);
  }
  DAT_010a09b0 = (undefined8 *)0x0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aee7fc"></a> `00aee7fc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aee800"></a> `00aee800` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee804"></a> `00aee804` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aee808"></a> `00aee808` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aee80c"></a> `00aee80c` | `95 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee810"></a> `00aee810` | `b3 da 44 f9` | ldr x19,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aee814"></a> `00aee814` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00aee818"></a> `00aee818` | `76 02 40 f9` | ldr x22,[x19] | `FALL_THROUGH`
<a id="insn-00aee81c"></a> `00aee81c` | `09 8d 40 f8` | ldr x9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00aee820"></a> `00aee820` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00aee824"></a> `00aee824` | `80 01 00 54` | b.eq 0x00aee854 | `CONDITIONAL_JUMP`
<a id="insn-00aee828"></a> `00aee828` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aee82c"></a> `00aee82c` | `c1 86 40 f8` | ldr x1,[x22], #0x8 | `FALL_THROUGH`
<a id="insn-00aee830"></a> `00aee830` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aee834"></a> `00aee834` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aee838"></a> `00aee838` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aee83c"></a> `00aee83c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aee840"></a> `00aee840` | `b3 da 44 f9` | ldr x19,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aee844"></a> `00aee844` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aee848"></a> `00aee848` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00aee84c"></a> `00aee84c` | `01 ff ff 54` | b.ne 0x00aee82c | `CONDITIONAL_JUMP`
<a id="insn-00aee850"></a> `00aee850` | `68 22 00 91` | add x8,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aee854"></a> `00aee854` | `f3 00 00 b4` | cbz x19,0x00aee870 | `CONDITIONAL_JUMP`
<a id="insn-00aee858"></a> `00aee858` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00aee85c"></a> `00aee85c` | `60 00 00 b4` | cbz x0,0x00aee868 | `CONDITIONAL_JUMP`
<a id="insn-00aee860"></a> `00aee860` | `00 01 00 f9` | str x0,[x8] | `FALL_THROUGH`
<a id="insn-00aee864"></a> `00aee864` | `bf b1 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aee868"></a> `00aee868` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee86c"></a> `00aee86c` | `bd b1 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aee870"></a> `00aee870` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aee874"></a> `00aee874` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee878"></a> `00aee878` | `bf da 04 f9` | str xzr,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aee87c"></a> `00aee87c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aee880"></a> `00aee880` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aee7fc`](#insn-00aee7fc) 範囲 `[['00aee7fc', '00aee827']]`
  - `CONDITIONAL_JUMP` [`00aee824`](#insn-00aee824) → [`00aee854`](#insn-00aee854)
  - `FALL_THROUGH` [`00aee824`](#insn-00aee824) → [`00aee828`](#insn-00aee828)
- ブロック [`00aee828`](#insn-00aee828) 範囲 `[['00aee828', '00aee82b']]`
  - `FALL_THROUGH` [`00aee828`](#insn-00aee828) → [`00aee82c`](#insn-00aee82c)
- ブロック [`00aee82c`](#insn-00aee82c) 範囲 `[['00aee82c', '00aee84f']]`
  - `CONDITIONAL_JUMP` [`00aee84c`](#insn-00aee84c) → [`00aee82c`](#insn-00aee82c)
  - `FALL_THROUGH` [`00aee84c`](#insn-00aee84c) → [`00aee850`](#insn-00aee850)
- ブロック [`00aee850`](#insn-00aee850) 範囲 `[['00aee850', '00aee853']]`
  - `FALL_THROUGH` [`00aee850`](#insn-00aee850) → [`00aee854`](#insn-00aee854)
- ブロック [`00aee854`](#insn-00aee854) 範囲 `[['00aee854', '00aee857']]`
  - `CONDITIONAL_JUMP` [`00aee854`](#insn-00aee854) → [`00aee870`](#insn-00aee870)
  - `FALL_THROUGH` [`00aee854`](#insn-00aee854) → [`00aee858`](#insn-00aee858)
- ブロック [`00aee858`](#insn-00aee858) 範囲 `[['00aee858', '00aee85f']]`
  - `CONDITIONAL_JUMP` [`00aee85c`](#insn-00aee85c) → [`00aee868`](#insn-00aee868)
  - `FALL_THROUGH` [`00aee85c`](#insn-00aee85c) → [`00aee860`](#insn-00aee860)
- ブロック [`00aee860`](#insn-00aee860) 範囲 `[['00aee860', '00aee867']]`
  - `FALL_THROUGH` [`00aee864`](#insn-00aee864) → [`00aee868`](#insn-00aee868)
- ブロック [`00aee868`](#insn-00aee868) 範囲 `[['00aee868', '00aee86f']]`
  - `FALL_THROUGH` [`00aee86c`](#insn-00aee86c) → [`00aee870`](#insn-00aee870)
- ブロック [`00aee870`](#insn-00aee870) 範囲 `[['00aee870', '00aee883']]`

## 命令位置別の参照

- [`00aee7fc`](#insn-00aee7fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee800`](#insn-00aee800) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee804`](#insn-00aee804) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee810`](#insn-00aee810) → `010a09b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee824`](#insn-00aee824) → [`00aee854`](#insn-00aee854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee840`](#insn-00aee840) → `010a09b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee84c`](#insn-00aee84c) → [`00aee82c`](#insn-00aee82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee854`](#insn-00aee854) → [`00aee870`](#insn-00aee870) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee85c`](#insn-00aee85c) → [`00aee868`](#insn-00aee868) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee864`](#insn-00aee864) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aee86c`](#insn-00aee86c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aee870`](#insn-00aee870) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee874`](#insn-00aee874) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee878`](#insn-00aee878) → `010a09b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aee7fc`](#insn-00aee7fc)

~~~json
{
  "source": "00aee7fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee800`](#insn-00aee800)

~~~json
{
  "source": "00aee800",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee804`](#insn-00aee804)

~~~json
{
  "source": "00aee804",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee810`](#insn-00aee810)

~~~json
{
  "source": "00aee810",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee824`](#insn-00aee824)

~~~json
{
  "source": "00aee824",
  "target": "00aee854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee840`](#insn-00aee840)

~~~json
{
  "source": "00aee840",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee84c`](#insn-00aee84c)

~~~json
{
  "source": "00aee84c",
  "target": "00aee82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee854`](#insn-00aee854)

~~~json
{
  "source": "00aee854",
  "target": "00aee870",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee85c`](#insn-00aee85c)

~~~json
{
  "source": "00aee85c",
  "target": "00aee868",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee864`](#insn-00aee864)

~~~json
{
  "source": "00aee864",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aee86c`](#insn-00aee86c)

~~~json
{
  "source": "00aee86c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aee870`](#insn-00aee870)

~~~json
{
  "source": "00aee870",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee874`](#insn-00aee874)

~~~json
{
  "source": "00aee874",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee878`](#insn-00aee878)

~~~json
{
  "source": "00aee878",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
