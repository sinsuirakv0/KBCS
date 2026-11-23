# 00aedff8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aee0c0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-fd4164daef4b6ab9629c7cbc01cd1795)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedff8",
  "name": "_ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96cfc0c2bcb8230e463b5528a61d87a77282c32e2030e125537f1d46ce872f03",
  "source_text_sha256": "96cfc0c2bcb8230e463b5528a61d87a77282c32e2030e125537f1d46ce872f03",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedff8",
        "00aee093"
      ]
    ],
    "bytes_sha256": "93741e4d82b4048b40945923fc7cae188152ed89c850e9560407da683c523e0d",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 604 bytes

~~~c

bool _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0990 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0988,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0990 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0990;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedff8"></a> `00aedff8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aedffc"></a> `00aedffc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee000"></a> `00aee000` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aee004"></a> `00aee004` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aee008"></a> `00aee008` | `95 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee00c"></a> `00aee00c` | `a8 42 66 39` | ldrb w8,[x21, #0x990] | `FALL_THROUGH`
<a id="insn-00aee010"></a> `00aee010` | `68 00 00 34` | cbz w8,0x00aee01c | `CONDITIONAL_JUMP`
<a id="insn-00aee014"></a> `00aee014` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aee018"></a> `00aee018` | `1b 00 00 14` | b 0x00aee084 | `UNCONDITIONAL_JUMP`
<a id="insn-00aee01c"></a> `00aee01c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aee020"></a> `00aee020` | `89 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aee024"></a> `00aee024` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aee028"></a> `00aee028` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aee02c"></a> `00aee02c` | `21 c5 44 f9` | ldr x1,[x9, #0x988] | `FALL_THROUGH`
<a id="insn-00aee030"></a> `00aee030` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aee034"></a> `00aee034` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aee038"></a> `00aee038` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aee03c"></a> `00aee03c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aee040"></a> `00aee040` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aee044"></a> `00aee044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee048"></a> `00aee048` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aee04c"></a> `00aee04c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aee050"></a> `00aee050` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aee054"></a> `00aee054` | `20 01 00 54` | b.eq 0x00aee078 | `CONDITIONAL_JUMP`
<a id="insn-00aee058"></a> `00aee058` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aee05c"></a> `00aee05c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee060"></a> `00aee060` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aee064"></a> `00aee064` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aee068"></a> `00aee068` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aee06c"></a> `00aee06c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aee070"></a> `00aee070` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aee074"></a> `00aee074` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aee078"></a> `00aee078` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aee07c"></a> `00aee07c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aee080"></a> `00aee080` | `a0 42 26 39` | strb w0,[x21, #0x990] | `FALL_THROUGH`
<a id="insn-00aee084"></a> `00aee084` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aee088"></a> `00aee088` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee08c"></a> `00aee08c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aee090"></a> `00aee090` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedff8`](#insn-00aedff8) 範囲 `[['00aedff8', '00aee013']]`
  - `CONDITIONAL_JUMP` [`00aee010`](#insn-00aee010) → [`00aee01c`](#insn-00aee01c)
  - `FALL_THROUGH` [`00aee010`](#insn-00aee010) → [`00aee014`](#insn-00aee014)
- ブロック [`00aee014`](#insn-00aee014) 範囲 `[['00aee014', '00aee01b']]`
  - `UNCONDITIONAL_JUMP` [`00aee018`](#insn-00aee018) → [`00aee084`](#insn-00aee084)
- ブロック [`00aee01c`](#insn-00aee01c) 範囲 `[['00aee01c', '00aee057']]`
  - `CONDITIONAL_JUMP` [`00aee054`](#insn-00aee054) → [`00aee078`](#insn-00aee078)
  - `FALL_THROUGH` [`00aee054`](#insn-00aee054) → [`00aee058`](#insn-00aee058)
- ブロック [`00aee058`](#insn-00aee058) 範囲 `[['00aee058', '00aee077']]`
  - `FALL_THROUGH` [`00aee074`](#insn-00aee074) → [`00aee078`](#insn-00aee078)
- ブロック [`00aee078`](#insn-00aee078) 範囲 `[['00aee078', '00aee083']]`
  - `FALL_THROUGH` [`00aee080`](#insn-00aee080) → [`00aee084`](#insn-00aee084)
- ブロック [`00aee084`](#insn-00aee084) 範囲 `[['00aee084', '00aee093']]`

## 命令位置別の参照

- [`00aedff8`](#insn-00aedff8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedffc`](#insn-00aedffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee000`](#insn-00aee000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee00c`](#insn-00aee00c) → `010a0990`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aee010`](#insn-00aee010) → [`00aee01c`](#insn-00aee01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee018`](#insn-00aee018) → [`00aee084`](#insn-00aee084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee02c`](#insn-00aee02c) → `010a0988`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee054`](#insn-00aee054) → [`00aee078`](#insn-00aee078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee080`](#insn-00aee080) → `010a0990`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aee084`](#insn-00aee084) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee088`](#insn-00aee088) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedff8`](#insn-00aedff8)

~~~json
{
  "source": "00aedff8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedffc`](#insn-00aedffc)

~~~json
{
  "source": "00aedffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee000`](#insn-00aee000)

~~~json
{
  "source": "00aee000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee00c`](#insn-00aee00c)

~~~json
{
  "source": "00aee00c",
  "target": "010a0990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0990",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee010`](#insn-00aee010)

~~~json
{
  "source": "00aee010",
  "target": "00aee01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee018`](#insn-00aee018)

~~~json
{
  "source": "00aee018",
  "target": "00aee084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee02c`](#insn-00aee02c)

~~~json
{
  "source": "00aee02c",
  "target": "010a0988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0988",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee054`](#insn-00aee054)

~~~json
{
  "source": "00aee054",
  "target": "00aee078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee080`](#insn-00aee080)

~~~json
{
  "source": "00aee080",
  "target": "010a0990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0990",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee084`](#insn-00aee084)

~~~json
{
  "source": "00aee084",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee088`](#insn-00aee088)

~~~json
{
  "source": "00aee088",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
