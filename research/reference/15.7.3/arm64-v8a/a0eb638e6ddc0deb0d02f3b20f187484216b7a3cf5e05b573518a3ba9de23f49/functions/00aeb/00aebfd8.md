# 00aebfd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebf10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebf10.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-3fce4e62ff4a30c813c16df3c5618e69)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aec01c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-73c39ebf0181c1cc6440a534a27d79f9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebfd8",
  "name": "_ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f2b329fa117fe48050ddee68c7ec1a444192e6d12a9bb157d355e06a76eddadd",
  "source_text_sha256": "f2b329fa117fe48050ddee68c7ec1a444192e6d12a9bb157d355e06a76eddadd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebfd8",
        "00aec073"
      ]
    ],
    "bytes_sha256": "06f654f4b6a70257061fe5c40994522875578ffb9a6199447e35026453ac7bd2",
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

## 疑似コード / UTF-8 699 bytes

~~~c

bool _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a08e8 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a08e0,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
                    /* try { // try from 00aec03c to 00bec047 has its CatchHandler @ 00af1b68 */
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a08e8 = iVar3 == 0;
    bVar2 = (bool)DAT_010a08e8;
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
<a id="insn-00aebfd8"></a> `00aebfd8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aebfdc"></a> `00aebfdc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebfe0"></a> `00aebfe0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebfe4"></a> `00aebfe4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aebfe8"></a> `00aebfe8` | `b5 2d 00 b0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebfec"></a> `00aebfec` | `a8 a2 63 39` | ldrb w8,[x21, #0x8e8] | `FALL_THROUGH`
<a id="insn-00aebff0"></a> `00aebff0` | `68 00 00 34` | cbz w8,0x00aebffc | `CONDITIONAL_JUMP`
<a id="insn-00aebff4"></a> `00aebff4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aebff8"></a> `00aebff8` | `1b 00 00 14` | b 0x00aec064 | `UNCONDITIONAL_JUMP`
<a id="insn-00aebffc"></a> `00aebffc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aec000"></a> `00aec000` | `a9 2d 00 90` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec004"></a> `00aec004` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aec008"></a> `00aec008` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aec00c"></a> `00aec00c` | `21 71 44 f9` | ldr x1,[x9, #0x8e0] | `FALL_THROUGH`
<a id="insn-00aec010"></a> `00aec010` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aec014"></a> `00aec014` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aec018"></a> `00aec018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec01c"></a> `00aec01c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec020"></a> `00aec020` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aec024"></a> `00aec024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec028"></a> `00aec028` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aec02c"></a> `00aec02c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec030"></a> `00aec030` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aec034"></a> `00aec034` | `20 01 00 54` | b.eq 0x00aec058 | `CONDITIONAL_JUMP`
<a id="insn-00aec038"></a> `00aec038` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec03c"></a> `00aec03c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec040"></a> `00aec040` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aec044"></a> `00aec044` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec048"></a> `00aec048` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec04c"></a> `00aec04c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec050"></a> `00aec050` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aec054"></a> `00aec054` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec058"></a> `00aec058` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aec05c"></a> `00aec05c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aec060"></a> `00aec060` | `a0 a2 23 39` | strb w0,[x21, #0x8e8] | `FALL_THROUGH`
<a id="insn-00aec064"></a> `00aec064` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aec068"></a> `00aec068` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec06c"></a> `00aec06c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aec070"></a> `00aec070` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebfd8`](#insn-00aebfd8) 範囲 `[['00aebfd8', '00aebff3']]`
  - `CONDITIONAL_JUMP` [`00aebff0`](#insn-00aebff0) → [`00aebffc`](#insn-00aebffc)
  - `FALL_THROUGH` [`00aebff0`](#insn-00aebff0) → [`00aebff4`](#insn-00aebff4)
- ブロック [`00aebff4`](#insn-00aebff4) 範囲 `[['00aebff4', '00aebffb']]`
  - `UNCONDITIONAL_JUMP` [`00aebff8`](#insn-00aebff8) → [`00aec064`](#insn-00aec064)
- ブロック [`00aebffc`](#insn-00aebffc) 範囲 `[['00aebffc', '00aec037']]`
  - `CONDITIONAL_JUMP` [`00aec034`](#insn-00aec034) → [`00aec058`](#insn-00aec058)
  - `FALL_THROUGH` [`00aec034`](#insn-00aec034) → [`00aec038`](#insn-00aec038)
- ブロック [`00aec038`](#insn-00aec038) 範囲 `[['00aec038', '00aec03b']]`
  - `FALL_THROUGH` [`00aec038`](#insn-00aec038) → [`00aec03c`](#insn-00aec03c)
- ブロック [`00aec03c`](#insn-00aec03c) 範囲 `[['00aec03c', '00aec057']]`
  - `FALL_THROUGH` [`00aec054`](#insn-00aec054) → [`00aec058`](#insn-00aec058)
- ブロック [`00aec058`](#insn-00aec058) 範囲 `[['00aec058', '00aec063']]`
  - `FALL_THROUGH` [`00aec060`](#insn-00aec060) → [`00aec064`](#insn-00aec064)
- ブロック [`00aec064`](#insn-00aec064) 範囲 `[['00aec064', '00aec073']]`

## 命令位置別の参照

- [`00aebfd8`](#insn-00aebfd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfdc`](#insn-00aebfdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfe0`](#insn-00aebfe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfec`](#insn-00aebfec) → `010a08e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aebff0`](#insn-00aebff0) → [`00aebffc`](#insn-00aebffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebff8`](#insn-00aebff8) → [`00aec064`](#insn-00aec064) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec00c`](#insn-00aec00c) → `010a08e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec034`](#insn-00aec034) → [`00aec058`](#insn-00aec058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec060`](#insn-00aec060) → `010a08e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aec064`](#insn-00aec064) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec068`](#insn-00aec068) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebfd8`](#insn-00aebfd8)

~~~json
{
  "source": "00aebfd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfdc`](#insn-00aebfdc)

~~~json
{
  "source": "00aebfdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfe0`](#insn-00aebfe0)

~~~json
{
  "source": "00aebfe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfec`](#insn-00aebfec)

~~~json
{
  "source": "00aebfec",
  "target": "010a08e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebff0`](#insn-00aebff0)

~~~json
{
  "source": "00aebff0",
  "target": "00aebffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebff8`](#insn-00aebff8)

~~~json
{
  "source": "00aebff8",
  "target": "00aec064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec00c`](#insn-00aec00c)

~~~json
{
  "source": "00aec00c",
  "target": "010a08e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec034`](#insn-00aec034)

~~~json
{
  "source": "00aec034",
  "target": "00aec058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec060`](#insn-00aec060)

~~~json
{
  "source": "00aec060",
  "target": "010a08e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec064`](#insn-00aec064)

~~~json
{
  "source": "00aec064",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec068`](#insn-00aec068)

~~~json
{
  "source": "00aec068",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
