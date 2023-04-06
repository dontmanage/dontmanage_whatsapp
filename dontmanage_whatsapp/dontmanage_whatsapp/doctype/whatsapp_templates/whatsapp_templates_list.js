dontmanage.listview_settings['WhatsApp Templates'] = {

	onload: function(listview) {
		listview.page.add_menu_item(__("Fetch templates from meta"), function() {
			dontmanage.call({
				method:'dontmanage_whatsapp.dontmanage_whatsapp.doctype.whatsapp_templates.whatsapp_templates.fetch',
				callback: function(res) {
					dontmanage.msgprint(res.message)
					listview.refresh();
				}
			});
		});
	}
};