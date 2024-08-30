import json


def _fixform(data):
    for form_i, form in enumerate(data["forms"]):
        for formitem_i, formitem in enumerate(form["formitems"]):
            value = formitem["value"]
            if isinstance(value, int):
                data["forms"][form_i]["formitems"][formitem_i]["value"] = str(value)
    return data


def request(flow):
    if flow.request.method == "POST" and flow.request.path == "/upload":
        for key, value in flow.request.multipart_form.items():
            if key == b"form":
                fixed = json.dumps(_fixform(json.loads(value)))
                flow.request.multipart_form[key] = fixed.encode("utf-8")
                break
